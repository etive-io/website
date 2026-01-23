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
        url = f"https://zenodo.org/api/records"
        params = {
            "q": f"conceptrecid:{ZENODO_CONCEPT_ID}",
            "sort": "mostrecent",
            "size": 50,
            "all_versions": True
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
        
        return {"releases": releases, "last_updated": datetime.utcnow().isoformat() + "Z"}
    except Exception as e:
        print(f"Error fetching Zenodo releases: {e}")
        return {"releases": [], "last_updated": datetime.utcnow().isoformat() + "Z"}

def main():
    """Fetch releases and write to JSON file."""
    print(f"Fetching asimov releases from Zenodo (concept: {ZENODO_CONCEPT_ID})...")
    
    data = fetch_zenodo_releases()
    
    # Write to file
    output_path = Path(__file__).parent.parent / "_data" / "zenodo-releases.json"
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    
    print(f"Found {len(data['releases'])} releases")
    print(f"Updated {output_path}")

if __name__ == "__main__":
    main()
