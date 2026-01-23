#!/usr/bin/env python3
"""
Update package statistics from PyPI, conda-forge, and GitHub.

This script fetches download statistics for asimov and related packages
from PyPI (via pepy.tech API), conda-forge (via conda-forge API), and
GitHub (via GitHub API), then updates the _data/package-stats.json file.
"""

import json
import requests
import os
from datetime import datetime
from pathlib import Path

# Packages to track with their GitHub repositories
PACKAGES = {
    "asimov": {
        "github_repo": "etive-io/asimov",
        "conda_forge_name": "asimov",
    },
    "asimov-bilby": {
        "github_repo": "transientlunatic/asimov-bilby",
        "conda_forge_name": "asimov-bilby",
    },
    "asimov-bayeswave": {
        "github_repo": "transientlunatic/asimov-bayeswave",
        "conda_forge_name": "asimov-bayeswave",
    },
    "asimov-cogwheel": {
        "github_repo": "etive-io/asimov-cogwheel",
        "conda_forge_name": "asimov-cogwheel",
    },
    "asimov-pycbc": {
        "github_repo": "etive-io/asimov-pycbc",
        "conda_forge_name": "asimov-pycbc",
    },
    "asimov-gwdata": {
        "github_repo": "etive-io/asimov-gwdata",
        "conda_forge_name": "asimov-gwdata",
    },
    "asimov-pyomicron": {
        "github_repo": "transientlunatic/asimov-pyomicron",
        "conda_forge_name": "asimov-pyomicron",
    },
    "asimov-pastro": {
        "github_repo": "transientlunatic/asimov-pastro",
        "conda_forge_name": "asimov-pastro",
    },
    "minke": {
        "github_repo": "etive-io/minke",
        "conda_forge_name": "minke",
    },
}

def get_github_stats(github_repo, github_token=None):
    """
    Fetch GitHub repository statistics.
    
    Returns stars count and latest release information.
    """
    try:
        # GitHub API for repo info
        url = f"https://api.github.com/repos/{github_repo}"
        headers = {}
        if github_token:
            headers["Authorization"] = f"token {github_token}"
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        repo_data = response.json()
        
        stars = repo_data.get("stargazers_count", 0)
        
        # Fetch latest release
        latest_release = None
        release_date = None
        
        try:
            releases_url = f"https://api.github.com/repos/{github_repo}/releases/latest"
            releases_response = requests.get(releases_url, headers=headers, timeout=10)
            if releases_response.status_code == 200:
                release_data = releases_response.json()
                latest_release = release_data.get("tag_name")
                release_date = release_data.get("published_at")
        except Exception as e:
            print(f"  Warning: Could not fetch latest release for {github_repo}: {e}")
        
        return {
            "stars": stars,
            "latest_release": latest_release,
            "release_date": release_date,
        }
    except Exception as e:
        print(f"Error fetching GitHub stats for {github_repo}: {e}")
        return {
            "stars": 0,
            "latest_release": None,
            "release_date": None,
        }

def get_pypi_stats(package_name):
    """
    Fetch PyPI download statistics using pepy.tech API.
    
    pepy.tech provides download stats for PyPI packages.
    Falls back gracefully if package not found or endpoint unavailable.
    """
    try:
        # pepy.tech API: https://pepy.tech/api/projects/{package}
        url = f"https://pepy.tech/api/projects/{package_name}"
        response = requests.get(url, timeout=10)
        
        # Handle 403 Forbidden or 404 Not Found gracefully
        if response.status_code in [403, 404]:
            print(f"  Info: PyPI stats not available for {package_name} (status {response.status_code})")
            return {"downloads_week": 0, "downloads_month": 0}
        
        response.raise_for_status()
        data = response.json()
        
        return {
            "downloads_week": data.get("downloads", {}).get("last_week", 0),
            "downloads_month": data.get("downloads", {}).get("last_month", 0),
        }
    except requests.exceptions.HTTPError as e:
        print(f"  Warning: HTTP error fetching PyPI stats for {package_name}: {e}")
        return {"downloads_week": 0, "downloads_month": 0}
    except Exception as e:
        print(f"  Warning: Error fetching PyPI stats for {package_name}: {e}")
        return {"downloads_week": 0, "downloads_month": 0}

def get_conda_forge_stats(package_name):
    """
    Fetch conda-forge download statistics.
    
    Uses the conda-forge API to get package download counts.
    Falls back gracefully if package not found or endpoint unavailable.
    """
    try:
        # conda-forge API for recent downloads
        url = f"https://api.anaconda.org/api/packages/conda-forge/{package_name}"
        response = requests.get(url, timeout=10)
        
        # Handle 404 Not Found gracefully - not all packages are on conda-forge
        if response.status_code == 404:
            print(f"  Info: Package {package_name} not found on conda-forge")
            return {"downloads_month": 0}
        
        response.raise_for_status()
        data = response.json()
        
        # Note: conda-forge API doesn't directly provide weekly/monthly stats
        # We return total downloads; you may want to use Quetz API for more detailed stats
        return {
            "downloads_month": data.get("downloads", 0),
        }
    except requests.exceptions.HTTPError as e:
        print(f"  Warning: HTTP error fetching conda-forge stats for {package_name}: {e}")
        return {"downloads_month": 0}
    except Exception as e:
        print(f"  Warning: Error fetching conda-forge stats for {package_name}: {e}")
        return {"downloads_month": 0}

def update_stats():
    """Update statistics for all packages."""
    stats = []
    github_token = os.environ.get("GITHUB_TOKEN")
    
    for package_name, package_info in PACKAGES.items():
        print(f"Fetching stats for {package_name}...")
        
        github_repo = package_info["github_repo"]
        conda_name = package_info["conda_forge_name"]
        
        # Get GitHub stats
        github_stats = get_github_stats(github_repo, github_token)
        
        # Get PyPI stats
        pypi_stats = get_pypi_stats(package_name)
        
        # Get conda-forge stats
        conda_stats = get_conda_forge_stats(conda_name)
        
        # Combine stats
        package_stats = {
            "name": package_name,
            "github_repo": github_repo,
            "github_stars": github_stats.get("stars", 0),
            "latest_release": github_stats.get("latest_release"),
            "release_date": github_stats.get("release_date"),
            "pypi_downloads_week": pypi_stats.get("downloads_week", 0),
            "pypi_downloads_month": pypi_stats.get("downloads_month", 0),
            "conda_forge_downloads_month": conda_stats.get("downloads_month", 0),
            "last_updated": datetime.utcnow().isoformat() + "Z",
        }
        
        stats.append(package_stats)
        print(f"  GitHub: ⭐ {package_stats['github_stars']} stars")
        if package_stats['latest_release']:
            print(f"  Latest Release: {package_stats['latest_release']}")
        print(f"  PyPI (week): {package_stats['pypi_downloads_week']}, "
              f"(month): {package_stats['pypi_downloads_month']}")
        print(f"  conda-forge (month): {package_stats['conda_forge_downloads_month']}")
    
    # Write to file
    output_path = Path(__file__).parent.parent / "_data" / "package-stats.json"
    with open(output_path, "w") as f:
        json.dump(stats, f, indent=2)
    
    print(f"\nUpdated {output_path}")

if __name__ == "__main__":
    update_stats()
