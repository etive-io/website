# GitHub Workflows

This directory contains automated workflows for the etive.io website.

## Workflows

### jekyll.yml
Builds and deploys the Jekyll site to GitHub Pages on every push to the master branch.

### update-releases.yml
Automatically fetches release information from GitHub for all ecosystem projects and updates `_data/releases.yml`.

**Schedule:** Runs daily at 00:00 UTC

**Manual trigger:** Can be triggered manually from the Actions tab

**What it does:**
1. Fetches the latest release information for all projects listed in `_data/projects.yml`
2. For each project, retrieves:
   - Latest release version and date
   - Up to 5 most recent releases
3. Updates `_data/releases.yml` with the fetched data
4. Commits and pushes changes if there are updates

**Data structure:**
The generated `_data/releases.yml` file contains:
- `last_updated`: Timestamp of when the data was fetched
- `projects`: Array of project release information, each containing:
  - `name`: Project name
  - `latest_release`: Latest version, name, date, and URL
  - `recent_releases`: List of recent releases

This data is automatically used by the releases page to display current version information.

## Setup

No additional setup is required. The workflow uses the repository's `GITHUB_TOKEN` which is automatically available in GitHub Actions.

## Testing

To test the release update workflow manually:
1. Go to the Actions tab in the GitHub repository
2. Select "Update Release Data" workflow
3. Click "Run workflow"
4. Select the branch and click "Run workflow"

The workflow will fetch release data and commit it to the repository if there are changes.
