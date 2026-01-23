#!/usr/bin/env python3
"""
Fetch papers citing asimov from NASA ADS.

This script queries the NASA ADS API for all papers that cite asimov
and stores the metadata for display on the impact page.

Note: This requires a valid ADS API key. Since the ADS API's citations() 
syntax requires special access, we gracefully fall back if unavailable.
"""

import json
import requests
import os
from datetime import datetime
from pathlib import Path

# The asimov JOSS paper bibcode
ASIMOV_BIBCODE = "2023JOSS....8.4170W"

def get_ads_api_key():
    """Get ADS API key from environment."""
    return os.environ.get("ADS_API_KEY")

def fetch_citing_papers():
    """
    Fetch papers citing asimov from NASA ADS.
    
    Uses the NASA ADS API to query for citations.
    Requires ADS_API_KEY environment variable.
    
    Note: The ADS API has specific requirements for citations queries.
    If the API is unavailable, we return gracefully.
    """
    api_key = get_ads_api_key()
    
    if not api_key:
        print("Info: ADS_API_KEY not set. Citing papers data will not be updated.")
        return {"papers": [], "total_citations": 0, "last_updated": datetime.utcnow().isoformat() + "Z"}
    
    try:
        # ADS API endpoint for search
        url = "https://api.adsabs.harvard.edu/v1/search/query"
        
        headers = {
            "Authorization": f"Bearer {api_key}"
        }
        
        # Query for papers that cite asimov
        # Using GET request with query parameters (not POST with JSON body)
        params = {
            "q": f'citations(bibcode:{ASIMOV_BIBCODE})',
            "rows": 100,
            "start": 0,
            "sort": "date desc",
            "fl": "title,author,year,bibcode,pub,pubdate,abstract,citation_count"
        }
        
        response = requests.get(url, params=params, headers=headers, timeout=30)
        
        response.raise_for_status()
        
        data = response.json()
        papers = []
        
        for doc in data.get("response", {}).get("docs", []):
            # Determine domain from journal
            journal = doc.get("pub", "")
            domain = infer_domain(journal)
            
            paper = {
                "title": doc.get("title", [""])[0] if isinstance(doc.get("title"), list) else doc.get("title", ""),
                "authors": "; ".join(doc.get("author", [])) if doc.get("author") else "",
                "year": doc.get("year", ""),
                "journal": journal,
                "abstract": doc.get("abstract", ""),
                "citation_count": doc.get("citation_count", 0),
                "domain": domain,
                "url": f"https://ui.adsabs.harvard.edu/abs/{doc.get('bibcode', '')}/abstract",
                "bibcode": doc.get("bibcode", "")
            }
            papers.append(paper)
        
        total = data.get("response", {}).get("numFound", len(papers))
        print(f"Found {len(papers)} citing papers (total: {total})")
        
        return {
            "papers": papers,
            "total_citations": total,
            "last_updated": datetime.utcnow().isoformat() + "Z"
        }
    
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error fetching from ADS API: {e}")
        return {"papers": [], "total_citations": 0, "last_updated": datetime.utcnow().isoformat() + "Z"}
    except requests.exceptions.RequestException as e:
        print(f"Error fetching from ADS API: {e}")
        return {"papers": [], "total_citations": 0, "last_updated": datetime.utcnow().isoformat() + "Z"}
    except Exception as e:
        print(f"Error processing ADS response: {e}")
        return {"papers": [], "total_citations": 0, "last_updated": datetime.utcnow().isoformat() + "Z"}

def infer_domain(journal_name):
    """
    Infer the research domain from journal name.
    """
    journal_lower = journal_name.lower()
    
    if any(x in journal_lower for x in ["physical review", "nature", "science", "classical and quantum"]):
        return "Gravitational Waves"
    elif any(x in journal_lower for x in ["astrophysical", "monthly notices", "astronomy"]):
        return "Astrophysics"
    elif any(x in journal_lower for x in ["machine learning", "neural", "data science"]):
        return "Machine Learning"
    elif any(x in journal_lower for x in ["bioinformatics", "genomics", "computational biology"]):
        return "Computational Biology"
    elif any(x in journal_lower for x in ["climate", "earth science", "environmental"]):
        return "Earth Sciences"
    else:
        return "Other Sciences"

def main():
    """Fetch papers and write to JSON file."""
    print(f"Fetching papers citing asimov ({ASIMOV_BIBCODE}) from NASA ADS...")
    
    data = fetch_citing_papers()
    
    print(f"Found {len(data['papers'])} citing papers (total: {data['total_citations']})")
    
    # Write to data locations (Jekyll build + public asset)
    output_path = Path(__file__).parent.parent / "_data" / "citing-papers.json"
    public_path = Path(__file__).parent.parent / "assets" / "data" / "citing-papers.json"
    public_path.parent.mkdir(parents=True, exist_ok=True)
    for path in (output_path, public_path):
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Updated {path}")

if __name__ == "__main__":
    main()
