#!/usr/bin/env python3
"""
Fetch brand logos using Brandfetch API.

Usage:
    python scripts/fetch-logo.py nike.com
    python scripts/fetch-logo.py nike.com --output /path/to/save/logo.svg
    python scripts/fetch-logo.py nike.com slack.com n8n.io --output-dir ./logos
    python scripts/fetch-logo.py nike.com --type icon  # icon, logo, or symbol
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.error
from pathlib import Path

# Load API key from .env
def load_api_key():
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                if line.startswith("BRANDFETCH_API_KEY="):
                    return line.strip().split("=", 1)[1]

    # Fallback to environment variable
    return os.environ.get("BRANDFETCH_API_KEY")

API_KEY = load_api_key()
BRAND_API_URL = "https://api.brandfetch.io/v2/brands"

def fetch_brand(domain: str) -> dict:
    """Fetch brand data from Brandfetch API."""
    url = f"{BRAND_API_URL}/{domain}"

    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {API_KEY}")

    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        print(f"Error fetching {domain}: {e.code} {e.reason}")
        return None

def download_logo(url: str, output_path: Path) -> bool:
    """Download a logo file."""
    try:
        urllib.request.urlretrieve(url, output_path)
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

def get_best_logo(brand_data: dict, logo_type: str = "logo") -> dict:
    """
    Extract the best logo from brand data.

    logo_type: 'icon' (square), 'logo' (horizontal), 'symbol' (brandmark)
    """
    if not brand_data or "logos" not in brand_data:
        return None

    logos = brand_data.get("logos", [])

    # Find the requested type
    for logo in logos:
        if logo.get("type") == logo_type:
            # Prefer SVG, then PNG
            formats = logo.get("formats", [])
            for fmt in formats:
                if fmt.get("format") == "svg":
                    return {"url": fmt.get("src"), "format": "svg"}
            for fmt in formats:
                if fmt.get("format") == "png":
                    return {"url": fmt.get("src"), "format": "png"}

    # Fallback: any logo with SVG
    for logo in logos:
        formats = logo.get("formats", [])
        for fmt in formats:
            if fmt.get("format") == "svg":
                return {"url": fmt.get("src"), "format": "svg"}

    # Fallback: any logo with PNG
    for logo in logos:
        formats = logo.get("formats", [])
        for fmt in formats:
            if fmt.get("format") == "png":
                return {"url": fmt.get("src"), "format": "png"}

    return None

def main():
    parser = argparse.ArgumentParser(description="Fetch brand logos from Brandfetch")
    parser.add_argument("domains", nargs="+", help="Domain(s) to fetch logos for")
    parser.add_argument("--output", "-o", help="Output file path (single domain only)")
    parser.add_argument("--output-dir", "-d", help="Output directory (multiple domains)")
    parser.add_argument("--type", "-t", choices=["icon", "logo", "symbol"],
                        default="logo", help="Logo type to fetch")
    parser.add_argument("--info", "-i", action="store_true",
                        help="Print brand info without downloading")

    args = parser.parse_args()

    if not API_KEY:
        print("Error: BRANDFETCH_API_KEY not found in .env or environment")
        sys.exit(1)

    # Determine output directory
    if args.output_dir:
        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
    elif args.output:
        output_dir = Path(args.output).parent
    else:
        output_dir = Path(".")

    for domain in args.domains:
        print(f"\nFetching {domain}...")
        brand = fetch_brand(domain)

        if not brand:
            continue

        if args.info:
            print(f"  Name: {brand.get('name', 'N/A')}")
            print(f"  Domain: {brand.get('domain', 'N/A')}")
            print(f"  Logos available: {len(brand.get('logos', []))}")
            for logo in brand.get("logos", []):
                formats = [f.get("format") for f in logo.get("formats", [])]
                print(f"    - {logo.get('type')}: {', '.join(formats)}")
            continue

        logo = get_best_logo(brand, args.type)

        if not logo:
            print(f"  No {args.type} logo found for {domain}")
            continue

        # Determine output filename
        clean_domain = domain.replace(".", "-").replace("/", "-")
        if args.output and len(args.domains) == 1:
            output_path = Path(args.output)
        else:
            output_path = output_dir / f"{clean_domain}.{logo['format']}"

        print(f"  Downloading {logo['format'].upper()} to {output_path}")
        if download_logo(logo["url"], output_path):
            print(f"  Saved to {output_path}")

if __name__ == "__main__":
    main()
