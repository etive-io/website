# Setting Up NASA ADS API for Research Impact Page

The research impact page requires a NASA ADS API key to fetch papers that cite asimov. This document explains how to set it up.

## Getting an ADS API Key

1. Go to https://ui.adsabs.harvard.edu/user/settings/token
2. Login with your NASA ADS account (create one if needed)
3. Generate a new API token
4. Copy the token value

## Adding to GitHub Repository

1. Go to your repository settings: `https://github.com/owner/repo/settings/secrets/actions`
2. Click "New repository secret"
3. Name: `ADS_API_KEY`
4. Value: Paste your token
5. Click "Add secret"

## How It Works

- The GitHub Actions workflow runs every Monday at 2:00 AM UTC
- It calls `scripts/fetch-citing-papers.py` with the `ADS_API_KEY` environment variable
- The script queries the NASA ADS API for papers citing asimov (bibcode: `2023JOSS....8.4170W`)
- Results are saved to `_data/citing-papers.json`
- The Jekyll site loads this data and displays it on `/impact/`

## Testing Locally

To test the script locally:

```bash
# Set your API key
export ADS_API_KEY="your-api-token-here"

# Run the script
python scripts/fetch-citing-papers.py

# Check the output
cat _data/citing-papers.json
```

## Troubleshooting

- **No results**: Check that your API key is valid and has access to search citations
- **Rate limiting**: NASA ADS has rate limits; wait before running again
- **Empty papers**: The JOSS paper may not have many citations yet; check manually at:
  https://ui.adsabs.harvard.edu/abs/2023JOSS....8.4170W/citations

## Domain Detection

The script automatically categorizes papers by research domain based on journal name:
- Gravitational Waves
- Astrophysics
- Machine Learning
- Computational Biology
- Earth Sciences
- Other Sciences

You can customize the `infer_domain()` function in `scripts/fetch-citing-papers.py` to improve categorization.
