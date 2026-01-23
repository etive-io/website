#!/usr/bin/env python3
"""
Fetch asimov releases from Zenodo and store release information.

This script queries the Zenodo API for all releases of asimov and stores
the metadata (title, DOI, publication date) for display on the citing page.
"""

import json
import requests
from datetime import datetime
from pathlib import Path

# Zenodo concept ID for asimov (all versions)
ZENODO_CONCEPT_ID = "4024432"

def fetch_zenodo_releases():
    """
    Fetch all asimov releases from Zenodo.
    
    Uses the Zenodo REST API to get release metadata.
    """
    try:
        # Zenodo API endpoint for a concept (includes all versions)
        # Using the concept ID to get all versions of the record
        url = f"https://zenodo.org/api/records/18341753/versions"
        params = {
            "sort": "mostrecent",
            "size": "25"
        }
        
        response = requests.get(url, params=params, timeout=10)
        
        response.raise_for_status()
        data = response.json()
        
        releases = []
        for record in data.get("hits", {}).get("hits", []):
            release = {
                "title": record.get("title", ""),
                "doi": record.get("doi", ""),
                "created": record.get("created", ""),
                "links": {
                    "html": record.get("links", {}).get("html", f"https://zenodo.org/record/{record.get('id')}")
                }
            }
            releases.append(release)
        
        print(f"Found {len(releases)} releases")
        return {"releases": releases, "last_updated": datetime.utcnow().isoformat() + "Z"}
    except Exception as e:
        print(f"Error fetching Zenodo releases: {e}")
        return {"releases": [], "last_updated": datetime.utcnow().isoformat() + "Z"}

def main():
    """Fetch releases and write to JSON file."""
    print(f"Fetching asimov releases from Zenodo (concept: {ZENODO_CONCEPT_ID})...")
    
    data = fetch_zenodo_releases()
    
        # Write to data locations (Jekyll build + public asset)
        output_path = Path(__file__).parent.parent / "_data" / "zenodo-releases.json"
        public_path = Path(__file__).parent.parent / "assets" / "data" / "zenodo-releases.json"
    # Write to file
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
        public_path.parent.mkdir(parents=True, exist_ok=True)
        for path in (output_path, public_path):
            with open(path, "w") as f:
                json.dump(data, f, indent=2)
            print(f"Updated {path}")
    
    print(f"Found {len(data['releases'])} releases")
    print(f"Updated {output_path}")

if __name__ == "__main__":
    main()
