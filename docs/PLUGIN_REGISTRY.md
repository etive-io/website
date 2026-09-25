# Plugin registry: design and plan

## Problem

Before this change, the list of ecosystem packages was kept by hand in four places:
`_plugins/*.md` (one page per plugin), `_data/projects.yml`, the `PACKAGES` dict in
`scripts/update-stats.py`, and the release-fetching workflow. They had drifted apart.
The bilby page said `pip install asimov-bilby`, a package that doesn't exist.
asimov-gwdata's GitHub link pointed at a repository that doesn't exist. Descriptions,
statuses and install commands were copied by hand from each package, and the
category filters on the plugin page were a `console.log` placeholder. Adding a
plugin meant writing a page and editing three other files.

## Model

The design follows the [AiiDA plugin registry](https://aiidateam.github.io/aiida-registry/):
keep a minimal hand-curated index, and derive everything else from the packages.

**Curated (`registry.yml`):** name, repository, category, and optionally the PyPI name,
maintenance status (`official`/`community`), docs URL, `featured`, and a `deprecated`
note. These are editorial judgements that can't be fetched.

**Fetched at build time (`scripts/build-registry.py`):**

| Field | Source |
|---|---|
| version, release date, summary, licence, `requires-python`, development status | PyPI JSON API |
| asimov entry points (`asimov.pipelines`, `asimov.hooks.*`, `asimov.commands`, `asimov.monitor.states`) | `pyproject.toml` / `setup.cfg` / `setup.py` in the repository; if that can't be read, `entry_points.txt` in the published wheel, or the metadata in the sdist |
| description, topics, stars, archived flag, last activity, README, releases | GitHub REST API, or GitLab API v4 (e.g. git.ligo.org) |
| conda-forge availability and version | anaconda.org API |

The output is `_data/registry.json`. A Jekyll generator (`_plugins/registry_pages.rb`)
creates `/plugins/<slug>/` for each package, rendering its README with the
install commands, the entry points it provides, its release history and links.
When a source can't be reached, the previous snapshot's value is kept.

Entry points are the key field. They are what asimov actually loads, so the
registry lists what a package *does* (for example "pipeline: bilby, bilby_native")
rather than what someone once wrote about it, and a submission is valid only if it
registers at least one.

## Done in this change

1. `registry.yml` with 17 entries, including packages that weren't listed before
   (bilby_pipe and RIFT, which ship their own asimov integrations; asimov-jim,
   asimov-simplepe, asimov-pycwb, asimov-ptadata, asimov-exoplanet).
2. `scripts/build-registry.py` with `--check`, `--strict`, `--only` and `--discover`.
3. A generated page per plugin, and a browser at `/plugins/` with text search,
   category facets, a "provides" filter by entry-point group, and toggles for
   team-maintained, on-PyPI and deprecated packages. Filter state is kept in the URL hash so
   filtered views can be linked.
4. `/pipelines/` now redirects to `/plugins/#provides=asimov.pipelines`, and the
   hand-written `_plugins/*.md` pages have been removed.
5. CI: the deploy workflow refreshes the registry before every build and rebuilds
   daily. `registry-check.yml` validates PRs to `registry.yml`, checks changed
   entries in strict mode and uploads a site preview. The old release-fetching
   workflow and `_data/projects.yml` / `_data/releases.yml` are gone: releases
   come from the registry.
6. `update-stats.py` takes its package list from `registry.yml`.
7. An issue form (`List a plugin`) for people who'd rather not open a PR.

## Next steps

These are listed roughly by value for effort.

1. **Auto-discovery PRs.** Run `build-registry.py --discover` weekly and open a PR that
   adds any public repository tagged `asimov-plugin` which isn't yet listed. Listing
   then only requires tagging the repository.
2. **Compatibility checks.** In a scheduled job, `pip install asimov <plugin>` in a
   clean environment and check that `importlib.metadata.entry_points()` resolves
   each advertised entry point against the latest asimov release, as AiiDA's
   registry does. Show the result as a badge ("works with asimov 0.7").
3. **Plugin metadata inside the package.** Read an optional
   `[tool.asimov.plugin]` table in `pyproject.toml` (category, docs,
   maintainer) so authors can move even the curated fields into their own
   repository, leaving `registry.yml` as a list of repositories.
4. **Blueprint examples.** Where a plugin repository has `examples/*.yaml`
   blueprints, show them on the plugin page as a "use it" snippet.
5. **README badge.** Serve `/plugins/<slug>/badge.svg` ("listed in the asimov
   registry") for plugin authors to link back.
6. **Registry JSON API.** Publish `_data/registry.json` at `/plugins/registry.json`
   so asimov itself could offer something like `asimov plugins search`.
