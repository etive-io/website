#!/usr/bin/env python3
"""
Build the asimov plugin registry from ``registry.yml``.

``registry.yml`` is the only hand-maintained list of ecosystem packages. Each
entry needs a name, a repository and a category; everything else shown on the
site is fetched here from the package's own sources of truth:

* PyPI JSON API            -> version, summary, licence, requires-python,
                              development-status classifier, release date
* pyproject.toml / setup.cfg / setup.py in the repository
                           -> ``asimov.*`` entry points (what the package
                              actually registers with asimov)
* GitHub or GitLab API     -> description, topics, stars, archived flag,
                              last activity, README, releases
* anaconda.org API         -> conda-forge availability and version

Output is written to ``_data/registry.json``, which the Jekyll site renders
(``_plugins/registry_pages.rb`` generates one page per entry). When a source
cannot be reached, the value from the previous snapshot is kept, so a network
blip never blanks the site.

Usage::

    python scripts/build-registry.py            # fetch and write snapshot
    python scripts/build-registry.py --check    # validate registry.yml only
    python scripts/build-registry.py --discover # also list untracked GitHub
                                                # repos tagged `asimov-plugin`

Set ``GITHUB_TOKEN`` to avoid GitHub's 60 requests/hour anonymous limit.
"""

from __future__ import annotations

import argparse
import configparser
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, urlparse

import requests
import yaml

try:
    import tomllib
except ModuleNotFoundError:  # Python < 3.11
    import tomli as tomllib

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "registry.yml"
OUTPUT = ROOT / "_data" / "registry.json"
TIMEOUT = 20

# What each asimov entry-point group means, for display.
ENTRY_POINT_GROUPS = {
    "asimov.pipelines": "Pipeline",
    "asimov.hooks.applicator": "Applicator hook",
    "asimov.hooks.postmonitor": "Post-monitor hook",
    "asimov.hooks.filesource": "File source",
    "asimov.monitor.states": "Monitor state",
    "asimov.commands": "CLI command",
}

CATEGORIES = {
    "core": "Core",
    "parameter-estimation": "Parameter estimation",
    "data": "Data & noise characterisation",
    "search": "Searches & burst analyses",
    "post-processing": "Post-processing & results",
    "population": "Populations & catalogues",
    "simulation": "Simulation & injections",
    "integration": "Services & integrations",
    "other-domains": "Beyond gravitational waves",
}

MAINTENANCE = ("official", "community")

# Test fixtures that packages register alongside their real entry points.
TEST_ENTRY_POINT = re.compile(r"test|dummy|fake", re.I)

REQUIRED = {"name", "repo", "category"}
OPTIONAL = {"pypi", "conda", "docs", "maintenance", "summary", "featured", "deprecated"}


# ---------------------------------------------------------------------------
# HTTP


class Fetcher:
    def __init__(self, github_token=None):
        self.session = requests.Session()
        self.session.headers["User-Agent"] = "etive-io-registry-builder"
        self.github_token = github_token
        self.disabled_hosts: set[str] = set()
        self.warnings: list[str] = []

    def get(self, url, headers=None, params=None):
        host = urlparse(url).netloc
        if host in self.disabled_hosts:
            return None
        try:
            r = self.session.get(url, headers=headers, params=params, timeout=TIMEOUT)
        except requests.RequestException as exc:
            # Unreachable host: stop trying it for the rest of the run.
            self.disabled_hosts.add(host)
            self.warnings.append(f"{host} unreachable ({exc.__class__.__name__}); using snapshot values")
            return None
        if r.status_code in (401, 403, 429) and host == "api.github.com":
            self.disabled_hosts.add(host)
            self.warnings.append(f"GitHub API refused ({r.status_code}); using snapshot values")
            return None
        return r

    def json(self, url, **kwargs):
        r = self.get(url, **kwargs)
        if r is None or r.status_code != 200:
            return None
        try:
            return r.json()
        except ValueError:
            return None

    def text(self, url, **kwargs):
        r = self.get(url, **kwargs)
        if r is None or r.status_code != 200:
            return None
        return r.text


# ---------------------------------------------------------------------------
# Repository hosts


class GitHub:
    api = "https://api.github.com"

    def __init__(self, f: Fetcher, path):
        self.f, self.path = f, path
        self.url = f"https://github.com/{path}"
        self.branch = "HEAD"
        self.headers = {"Accept": "application/vnd.github+json"}
        if f.github_token:
            self.headers["Authorization"] = f"Bearer {f.github_token}"

    def raw(self, filename):
        return self.f.text(f"https://raw.githubusercontent.com/{self.path}/{self.branch}/{filename}")

    def metadata(self):
        meta = self.f.json(f"{self.api}/repos/{self.path}", headers=self.headers)
        if not meta:
            return None
        self.branch = meta.get("default_branch") or "HEAD"
        out = {
            "host": "GitHub",
            "url": meta["html_url"],
            "description": meta.get("description"),
            "topics": meta.get("topics", []),
            "stars": meta.get("stargazers_count", 0),
            "archived": meta.get("archived", False),
            "last_activity": (meta.get("pushed_at") or "")[:10] or None,
            "homepage": meta.get("homepage") or None,
        }
        readme = self.f.text(
            f"{self.api}/repos/{self.path}/readme",
            headers={**self.headers, "Accept": "application/vnd.github.html+json"},
        )
        if readme:
            out["readme"] = {"format": "html", "text": rewrite_relative_html(readme, self)}
        releases = self.f.json(
            f"{self.api}/repos/{self.path}/releases", headers=self.headers, params={"per_page": 5}
        ) or []
        out["releases"] = [
            {
                "version": r["tag_name"],
                "name": r.get("name") or r["tag_name"],
                "published_at": (r.get("published_at") or "")[:10] or None,
                "url": r["html_url"],
                "prerelease": r.get("prerelease", False),
            }
            for r in releases
            if not r.get("draft")
        ]
        return out

    def blob_url(self, filename):
        return f"{self.url}/blob/{self.branch}/{filename}"

    def raw_url(self, filename):
        return f"https://raw.githubusercontent.com/{self.path}/{self.branch}/{filename}"


class GitLab:
    def __init__(self, f: Fetcher, url):
        parsed = urlparse(url)
        self.f = f
        self.base = f"{parsed.scheme}://{parsed.netloc}"
        self.path = parsed.path.strip("/")
        self.url = f"{self.base}/{self.path}"
        self.api = f"{self.base}/api/v4/projects/{quote(self.path, safe='')}"
        self.branch = "HEAD"

    def raw(self, filename):
        return self.f.text(f"{self.url}/-/raw/{self.branch}/{filename}")

    def metadata(self):
        meta = self.f.json(self.api)
        if not meta:
            return None
        self.branch = meta.get("default_branch") or "HEAD"
        out = {
            "host": urlparse(self.base).netloc,
            "url": meta.get("web_url", self.url),
            "description": meta.get("description") or None,
            "topics": meta.get("topics") or meta.get("tag_list") or [],
            "stars": meta.get("star_count", 0),
            "archived": meta.get("archived", False),
            "last_activity": (meta.get("last_activity_at") or "")[:10] or None,
            "homepage": None,
        }
        readme = raw_readme(self)
        if readme:
            out["readme"] = readme
        releases = self.f.json(f"{self.api}/releases", params={"per_page": 5}) or []
        out["releases"] = [
            {
                "version": r["tag_name"],
                "name": r.get("name") or r["tag_name"],
                "published_at": (r.get("released_at") or "")[:10] or None,
                "url": (r.get("_links") or {}).get("self", f"{self.url}/-/releases/{r['tag_name']}"),
                "prerelease": r.get("upcoming_release", False),
            }
            for r in releases
        ]
        return out

    def blob_url(self, filename):
        return f"{self.url}/-/blob/{self.branch}/{filename}"

    def raw_url(self, filename):
        return f"{self.url}/-/raw/{self.branch}/{filename}"


def host_for(f: Fetcher, repo: str):
    if repo.startswith("http"):
        if urlparse(repo).netloc == "github.com":
            return GitHub(f, urlparse(repo).path.strip("/"))
        return GitLab(f, repo)
    return GitHub(f, repo)


# ---------------------------------------------------------------------------
# Readmes


def rewrite_relative_html(html, host):
    """Point README-relative links and images at the repository."""

    def fix(attr, base):
        def sub(m):
            url = m.group(2)
            if re.match(r"^(?:[a-z][a-z0-9+.-]*:|#|/|data:)", url, re.I):
                return m.group(0)
            return f"{attr}={m.group(1)}{base(url.lstrip('./'))}{m.group(1)}"
        return sub

    html = re.sub(r'src=(["\'])(.*?)\1', fix("src", host.raw_url), html)
    html = re.sub(r'href=(["\'])(.*?)\1', fix("href", host.blob_url), html)
    return html


def rewrite_relative_markdown(text, host):
    def sub(m):
        bang, label, url = m.group(1), m.group(2), m.group(3)
        if re.match(r"^(?:[a-z][a-z0-9+.-]*:|#|/)", url, re.I):
            return m.group(0)
        base = host.raw_url if bang else host.blob_url
        return f"{bang}[{label}]({base(url.lstrip('./'))})"

    return re.sub(r"(!?)\[([^\]]*)\]\(([^)\s]+)\)", sub, text)


def rst_to_html(text):
    try:
        from docutils.core import publish_parts
    except ImportError:
        return None
    try:
        return publish_parts(
            text,
            writer_name="html",
            settings_overrides={"report_level": 5, "halt_level": 5, "raw_enabled": False,
                                "file_insertion_enabled": False, "initial_header_level": 2},
        )["body"]
    except Exception:
        return None


def raw_readme(host):
    for name, fmt in (("README.md", "markdown"), ("README.rst", "rst"), ("README", "text")):
        text = host.raw(name)
        if text:
            if fmt == "markdown":
                text = rewrite_relative_markdown(text, host)
            elif fmt == "rst":
                html = rst_to_html(text)
                if html:
                    fmt, text = "html", rewrite_relative_html(html, host)
            return {"format": fmt, "text": text, "url": host.blob_url(name)}
    return None


# ---------------------------------------------------------------------------
# Entry points


def entry_points_from_pyproject(text):
    try:
        data = tomllib.loads(text)
    except Exception:
        return None
    eps = data.get("project", {}).get("entry-points", {})
    eps = eps or data.get("tool", {}).get("poetry", {}).get("plugins", {})
    return {g: sorted(v) for g, v in eps.items() if g.startswith("asimov")}


def entry_points_from_setup_cfg(text):
    cfg = configparser.ConfigParser()
    try:
        cfg.read_string(text)
    except configparser.Error:
        return None
    if not cfg.has_section("options.entry_points"):
        return {}
    out = {}
    for group, value in cfg.items("options.entry_points"):
        if group.startswith("asimov"):
            out[group] = sorted(l.split("=")[0].strip() for l in value.splitlines() if "=" in l)
    return out


def entry_points_from_setup_py(text):
    # Best effort: "'asimov.pipelines': ['name = mod:Cls', ...]"
    out = {}
    for group, body in re.findall(r"""['"](asimov[\w.]*)['"]\s*:\s*\[([^\]]*)\]""", text):
        out[group] = sorted(re.findall(r"""['"]\s*([\w-]+)\s*=""", body))
    return out


def pyproject_description(host):
    text = host.raw("pyproject.toml")
    if not text:
        return None
    try:
        return tomllib.loads(text).get("project", {}).get("description") or None
    except Exception:
        return None


def entry_points_from_wheel(f: Fetcher, wheel_urls):
    """Read entry_points.txt from a published wheel (what users actually install)."""
    import io
    import zipfile

    for url in wheel_urls[:1]:
        r = f.get(url)
        if r is None or r.status_code != 200:
            return None
        try:
            with zipfile.ZipFile(io.BytesIO(r.content)) as zf:
                name = next((n for n in zf.namelist() if n.endswith(".dist-info/entry_points.txt")), None)
                if not name:
                    return {}
                cfg = configparser.ConfigParser()
                cfg.read_string(zf.read(name).decode())
        except (zipfile.BadZipFile, configparser.Error, UnicodeDecodeError):
            return None
        return {g: sorted(cfg[g].keys()) for g in cfg.sections() if g.startswith("asimov")}
    return None


def entry_points_from_sdist(f: Fetcher, sdist_urls):
    """Parse packaging metadata inside a published source distribution."""
    import io
    import tarfile
    import zipfile

    for url in sdist_urls[:1]:
        r = f.get(url)
        if r is None or r.status_code != 200:
            return None
        files = {}
        try:
            if url.endswith(".zip"):
                with zipfile.ZipFile(io.BytesIO(r.content)) as zf:
                    for n in zf.namelist():
                        if n.count("/") == 1 and n.split("/")[1] in ("pyproject.toml", "setup.cfg", "setup.py"):
                            files[n.split("/")[1]] = zf.read(n).decode()
            else:
                with tarfile.open(fileobj=io.BytesIO(r.content), mode="r:*") as tf:
                    for m in tf.getmembers():
                        parts = m.name.split("/")
                        if len(parts) == 2 and parts[1] in ("pyproject.toml", "setup.cfg", "setup.py") and m.isfile():
                            files[parts[1]] = tf.extractfile(m).read().decode()
        except (tarfile.TarError, zipfile.BadZipFile, UnicodeDecodeError):
            return None
        for filename, parse in (
            ("pyproject.toml", entry_points_from_pyproject),
            ("setup.cfg", entry_points_from_setup_cfg),
            ("setup.py", entry_points_from_setup_py),
        ):
            if filename in files and (eps := parse(files[filename])):
                return eps
        return {}
    return None


def fetch_entry_points(host):
    for filename, parse in (
        ("pyproject.toml", entry_points_from_pyproject),
        ("setup.cfg", entry_points_from_setup_cfg),
        ("setup.py", entry_points_from_setup_py),
    ):
        text = host.raw(filename)
        if text:
            eps = parse(text)
            if eps:
                return eps
    return None


# ---------------------------------------------------------------------------
# Package indexes


NOT_FOUND = object()


def fetch_pypi(f: Fetcher, name):
    r = f.get(f"https://pypi.org/pypi/{name}/json")
    if r is not None and r.status_code == 404:
        return NOT_FOUND
    try:
        data = r.json() if r is not None and r.status_code == 200 else None
    except ValueError:
        data = None
    if not data:
        return None
    info = data["info"]
    version = info.get("version")
    files = data.get("releases", {}).get(version) or []
    uploaded = min((x["upload_time_iso_8601"] for x in files), default=None)
    licence = info.get("license_expression") or info.get("license") or None
    if licence and (len(licence) > 40 or "\n" in licence):  # full text pasted in
        licence = None
    if not licence:
        for c in info.get("classifiers", []):
            if c.startswith("License ::"):
                licence = c.split("::")[-1].strip()
    status = None
    for c in info.get("classifiers", []):
        m = re.match(r"Development Status :: \d+ - (.+)", c)
        if m:
            status = m.group(1)
    return {
        "name": info["name"],
        "version": version,
        "released": uploaded[:10] if uploaded else None,
        "summary": info.get("summary") or None,
        "requires_python": info.get("requires_python") or None,
        "license": licence,
        "status": status,
        "url": f"https://pypi.org/project/{info['name']}/",
        "_wheels": [x["url"] for x in data.get("urls", []) if x.get("packagetype") == "bdist_wheel"],
        "_sdists": [x["url"] for x in data.get("urls", []) if x.get("packagetype") == "sdist"],
    }


def fetch_conda(f: Fetcher, name):
    data = f.json(f"https://api.anaconda.org/package/conda-forge/{name}")
    if not data:
        return None
    return {
        "name": name,
        "version": data.get("latest_version"),
        "url": f"https://anaconda.org/conda-forge/{name}",
    }


# ---------------------------------------------------------------------------


def load_registry():
    with open(REGISTRY) as fh:
        return yaml.safe_load(fh) or []


def validate(entries):
    errors, seen = [], set()
    for i, e in enumerate(entries):
        where = e.get("name", f"entry {i}")
        if missing := REQUIRED - e.keys():
            errors.append(f"{where}: missing {sorted(missing)}")
        if unknown := e.keys() - REQUIRED - OPTIONAL:
            errors.append(f"{where}: unknown keys {sorted(unknown)}")
        if e.get("category") not in CATEGORIES:
            errors.append(f"{where}: category must be one of {sorted(CATEGORIES)}")
        if e.get("maintenance", "community") not in MAINTENANCE:
            errors.append(f"{where}: maintenance must be one of {list(MAINTENANCE)}")
        repo = str(e.get("repo", ""))
        if not (re.fullmatch(r"[\w.-]+/[\w.-]+", repo) or re.match(r"https://[\w.-]+/.+/.+", repo)):
            errors.append(f"{where}: repo must be 'owner/name' (GitHub) or a full https URL")
        if e.get("name") in seen:
            errors.append(f"{where}: duplicate name")
        seen.add(e.get("name"))
    return errors


def slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def build_one(f: Fetcher, e, prev):
    name = e["name"]
    host = host_for(f, e["repo"])
    rec = {
        "name": name,
        "slug": slugify(name),
        "repo": e["repo"],
        "repo_url": host.url,
        "category": e["category"],
        "category_label": CATEGORIES[e["category"]],
        "maintenance": e.get("maintenance", "community"),
        "featured": bool(e.get("featured", False)),
        "deprecated": e.get("deprecated") or None,
        "docs": e.get("docs") or None,
    }

    # Repository metadata first: it sets the default branch for raw fetches.
    meta = host.metadata()
    if meta is None:
        meta = dict(prev.get("source") or {})
        if "readme" not in meta:
            if readme := raw_readme(host):
                meta["readme"] = readme
    rec["source"] = meta

    pypi_name = e.get("pypi", name)
    rec["pypi"] = fetch_pypi(f, pypi_name) if pypi_name else NOT_FOUND
    if rec["pypi"] is None:  # index unreachable: keep what we knew
        rec["pypi"] = prev.get("pypi")
    elif rec["pypi"] is NOT_FOUND:
        rec["pypi"] = None
    conda_name = e.get("conda", pypi_name or name)
    rec["conda"] = (fetch_conda(f, conda_name) or prev.get("conda")) if conda_name else None

    eps = fetch_entry_points(host)
    if eps is None and rec["pypi"]:
        eps = entry_points_from_wheel(f, rec["pypi"].get("_wheels", []))
        if eps is None:
            eps = entry_points_from_sdist(f, rec["pypi"].get("_sdists", []))
    if rec["pypi"]:
        rec["pypi"].pop("_wheels", None)
        rec["pypi"].pop("_sdists", None)
    if eps is None:
        rec["entry_points"] = prev.get("entry_points", [])
    else:
        rec["entry_points"] = [
            {"group": g, "label": ENTRY_POINT_GROUPS.get(g, g), "names": shown}
            for g, names in sorted(eps.items())
            if (shown := [n for n in names if not TEST_ENTRY_POINT.search(n)])
        ]

    rec["summary"] = (
        e.get("summary")
        or (rec["pypi"] or {}).get("summary")
        or meta.get("description")
        or pyproject_description(host)
        or prev.get("summary")
        or ""
    )
    if meta.get("archived") and not rec["deprecated"]:
        rec["deprecated"] = "The repository has been archived."
    rec["docs"] = rec["docs"] or meta.get("homepage")

    if rec["pypi"]:
        rec["install"] = f"pip install {rec['pypi']['name']}"
    else:
        rec["install"] = f"pip install git+{host.url}"
    if rec["conda"]:
        rec["install_conda"] = f"conda install -c conda-forge {rec['conda']['name']}"

    # Release list: repository releases, falling back to the PyPI version.
    stable = next((r for r in meta.get("releases", []) if not r.get("prerelease")), {})
    rec["latest_version"] = (rec["pypi"] or {}).get("version") or stable.get("version")
    rec["latest_released"] = (rec["pypi"] or {}).get("released") or stable.get("published_at")
    return rec


def discover(f: Fetcher, known_repos):
    data = f.json(
        "https://api.github.com/search/repositories",
        headers=host_for(f, "a/b").headers,
        params={"q": "topic:asimov-plugin", "per_page": 100},
    )
    if not data:
        print("Discovery needs the GitHub API; skipped.", file=sys.stderr)
        return []
    known = {r.lower() for r in known_repos}
    return [
        {"repo": item["full_name"], "description": item.get("description")}
        for item in data.get("items", [])
        if item["full_name"].lower() not in known
    ]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="validate registry.yml and exit")
    ap.add_argument("--strict", action="store_true",
                    help="fail if a plugin exposes no asimov entry points or its repository can't be read")
    ap.add_argument("--only", nargs="*", metavar="NAME", help="only fetch these entries (others keep snapshot values)")
    ap.add_argument("--discover", action="store_true", help="report untracked repos tagged asimov-plugin")
    args = ap.parse_args()

    entries = load_registry()
    if errors := validate(entries):
        print("registry.yml has problems:\n  " + "\n  ".join(errors), file=sys.stderr)
        return 1
    if args.check:
        print(f"registry.yml OK ({len(entries)} entries)")
        return 0

    previous = {}
    if OUTPUT.exists():
        try:
            previous = {p["name"]: p for p in json.loads(OUTPUT.read_text())["packages"]}
        except (ValueError, KeyError):
            pass

    f = Fetcher(os.environ.get("GITHUB_TOKEN"))
    packages = []
    problems = []
    for e in entries:
        prev = previous.get(e["name"], {})
        if args.only is not None and e["name"] not in args.only and prev:
            packages.append(prev)
            continue
        print(f"· {e['name']}", file=sys.stderr)
        rec = build_one(f, e, prev)
        packages.append(rec)
        if e["category"] != "core":
            if not rec["entry_points"]:
                problems.append(f"{e['name']}: no asimov.* entry points found in the repository or on PyPI")
            if not rec["source"].get("readme") and not rec["pypi"]:
                problems.append(f"{e['name']}: repository {e['repo']} could not be read")

    snapshot = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "categories": [{"id": k, "label": v} for k, v in CATEGORIES.items()],
        "entry_point_groups": ENTRY_POINT_GROUPS,
        "packages": packages,
    }
    if args.discover:
        snapshot["discovered"] = discover(f, [e["repo"] for e in entries])

    OUTPUT.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n")
    for w in dict.fromkeys(f.warnings):
        print(f"warning: {w}", file=sys.stderr)
    print(f"Wrote {OUTPUT.relative_to(ROOT)} ({len(packages)} packages)")
    for p in problems:
        print(f"{'error' if args.strict else 'warning'}: {p}", file=sys.stderr)
    return 1 if (args.strict and problems) else 0


if __name__ == "__main__":
    sys.exit(main())
