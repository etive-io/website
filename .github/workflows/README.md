# Workflows

| Workflow | Trigger | What it does |
|---|---|---|
| `jekyll.yml` | push to `master`, daily, manual | Refreshes the plugin registry (`scripts/build-registry.py`), builds the site and deploys it to GitHub Pages. |
| `registry-check.yml` | pull requests touching `registry.yml` or the registry code | Validates `registry.yml`, fetches changed entries in `--strict` mode (the repository must be readable and register `asimov.*` entry points), builds the site and uploads it as a preview artifact. |
| `update-stats.yml` | weekly, manual | Fetches download counts, Zenodo releases and citing papers, commits them to `_data/`, and triggers a deploy. The package list comes from `registry.yml`. |

## The plugin registry

`registry.yml` is the only hand-maintained list of ecosystem packages. Everything
shown about a package (description, version, licence, Python support, entry
points, conda-forge availability, README, releases) is fetched at build time from
PyPI and the package's repository, then written to `_data/registry.json`.
`_plugins/registry_pages.rb` turns that file into one page per package under
`/plugins/<slug>/`.

`_data/registry.json` is committed as a snapshot. The build overwrites it with fresh
data, and keeps the snapshot value for anything it can't reach, so local builds work
offline and an outage at PyPI or GitHub never removes content from the site. To
refresh it locally:

```bash
pip install requests pyyaml docutils
GITHUB_TOKEN=... python scripts/build-registry.py     # token optional; avoids rate limits
python scripts/build-registry.py --discover           # also list untracked repos tagged asimov-plugin
```

No secrets are needed: the built-in `GITHUB_TOKEN` can read public repositories.
`update-stats.yml` optionally uses an `ADS_API_KEY` secret for citation data
(see `docs/ADS_API_SETUP.md`).
