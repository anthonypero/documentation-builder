# 1-scrape_links.py
import argparse
import sys
import os
import json
import re
import time
import xml.etree.ElementTree as ET
from datetime import datetime
from urllib.parse import urljoin, urlparse
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def slugify(text):
    """Converts a string into a URL-friendly slug."""
    if not text:
        return "untitled"
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    text = re.sub(r'[-\s]+', '-', text)
    return text


def humanize_path(path):
    """Converts a URL path segment into a human-readable title."""
    # Get the last segment of the path
    segment = path.rstrip('/').split('/')[-1]
    if not segment:
        return "Home"
    # Replace hyphens/underscores with spaces and title case
    return segment.replace('-', ' ').replace('_', ' ').title()


def discover_sitemap(docs_url):
    """
    Attempts to discover a sitemap for the given documentation URL.
    
    Args:
        docs_url (str): The documentation URL (e.g., https://example.com/docs)
        
    Returns:
        str or None: The sitemap URL if found, None otherwise.
    """
    parsed = urlparse(docs_url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    
    # List of sitemap locations to try
    candidates = [
        f"{docs_url.rstrip('/')}/sitemap.xml",  # /docs/sitemap.xml
        f"{base_url}/sitemap.xml",               # /sitemap.xml
    ]
    
    for candidate in candidates:
        try:
            req = Request(candidate, headers={'User-Agent': 'Mozilla/5.0'})
            response = urlopen(req, timeout=10)
            if response.status == 200:
                # Verify it's actually XML
                content = response.read(500).decode('utf-8', errors='ignore')
                if '<?xml' in content or '<urlset' in content:
                    print(f"Found sitemap: {candidate}")
                    return candidate
        except (URLError, HTTPError):
            continue
    
    # Try robots.txt for Sitemap directive
    try:
        robots_url = f"{base_url}/robots.txt"
        req = Request(robots_url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req, timeout=10)
        content = response.read().decode('utf-8', errors='ignore')
        for line in content.split('\n'):
            if line.lower().startswith('sitemap:'):
                sitemap_url = line.split(':', 1)[1].strip()
                print(f"Found sitemap in robots.txt: {sitemap_url}")
                return sitemap_url
    except (URLError, HTTPError):
        pass
    
    return None


def parse_sitemap(sitemap_url, path_prefix):
    """
    Parses a sitemap XML and extracts URLs matching the given path prefix.
    
    Args:
        sitemap_url (str): The URL of the sitemap.xml
        path_prefix (str): Only include URLs starting with this prefix
        
    Returns:
        list: A list of dictionaries with 'order', 'url', 'title', 'status', 'retry_count'
    """
    try:
        req = Request(sitemap_url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req, timeout=30)
        content = response.read()
        
        # Parse XML
        root = ET.fromstring(content)
        
        # Handle namespace
        ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        
        scraped_data = []
        unique_urls = set()
        
        # Normalize prefix for comparison
        prefix_normalized = path_prefix.rstrip('/')
        
        for index, url_elem in enumerate(root.findall('.//sm:url', ns)):
            loc = url_elem.find('sm:loc', ns)
            if loc is not None and loc.text:
                url = loc.text.strip()
                
                # Filter by path prefix
                if not url.startswith(prefix_normalized):
                    continue
                
                # Deduplicate
                url_normalized = url.rstrip('/')
                if url_normalized in unique_urls:
                    continue
                unique_urls.add(url_normalized)
                
                scraped_data.append({
                    'order': len(scraped_data),
                    'url': url,
                    'title': humanize_path(url),
                    'status': 'pending',
                    'retry_count': 0
                })
        
        return scraped_data
        
    except Exception as e:
        print(f"Error parsing sitemap: {e}", file=sys.stderr)
        return []


def scrape_links(url, nav_selector):
    """
    Scrapes all unique, absolute links from a navigation element on a given URL.
    
    Args:
        url (str): The URL to scrape.
        nav_selector (str): The CSS selector for the navigation element.
        
    Returns:
        list: A list of dictionaries, each containing 'order', 'url', and 'title'.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    # Suppress webdriver-manager logs
    os.environ['WDM_LOG_LEVEL'] = '0'

    try:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        driver.get(url)
        
        # Wait for the navigation element to be present
        driver.implicitly_wait(10)
        
        nav_element = driver.find_element(By.CSS_SELECTOR, nav_selector)

        # Expand all collapsible elements before collecting links
        # Targeted at Docusaurus (.menu__list-item--collapsed) and ARIA standards
        last_expandable_count = -1
        while True:
            expandables = nav_element.find_elements(By.CSS_SELECTOR, "[aria-expanded='false'], .menu__list-item--collapsed")
            if not expandables or len(expandables) == last_expandable_count:
                break
            last_expandable_count = len(expandables)
            for expandable in expandables:
                try:
                    driver.execute_script("arguments[0].click();", expandable)
                    time.sleep(0.1)
                except:
                    continue
        
        # Collect ALL [href] descendants
        link_elements = nav_element.find_elements(By.CSS_SELECTOR, "[href]")
        
        scraped_data = []
        unique_urls = set()
        
        base_url_parts = urlparse(url)

        for index, link_element in enumerate(link_elements):
            href = link_element.get_attribute('href')
            title = link_element.get_attribute('textContent').strip()

            if href:
                absolute_url = urljoin(url, href)
                url_to_check = urljoin(absolute_url, urlparse(absolute_url).path)

                if url_to_check not in unique_urls and urlparse(absolute_url).scheme in ['http', 'https']:
                    link_parts = urlparse(absolute_url)
                    if link_parts.netloc == base_url_parts.netloc:
                        unique_urls.add(url_to_check)
                        scraped_data.append({
                            'order': index,
                            'url': absolute_url,
                            'title': title if title else "Untitled",
                            'status': 'pending',
                            'retry_count': 0
                        })

    except Exception as e:
        print(f"An error occurred during scraping: {e}", file=sys.stderr)
        return []
    finally:
        if 'driver' in locals():
            driver.quit()
            
    return scraped_data


def main():
    parser = argparse.ArgumentParser(description="Scrape links from a webpage's navigation element or sitemap.")
    parser.add_argument("--project-dir", required=True, help="Path to the project directory.")
    parser.add_argument("--url", required=True, help="The URL to scrape.")
    parser.add_argument("--selector", default="", help="The CSS selector for the navigation element.")
    parser.add_argument("--title", required=True, help="Human-readable title for the documentation.")
    parser.add_argument("--id", required=True, help="Slugified ID for the project.")
    parser.add_argument("--section", default="", help="CSS selector for the main content section.")
    parser.add_argument("--sitemap", action="store_true", help="Use sitemap for URL discovery instead of sidebar (for obfuscated sidebars).")
    parser.add_argument("--update", action="store_true", help="Update existing manifest (increment version).")

    
    args = parser.parse_args()
    
    manifest_path = os.path.join(args.project_dir, 'manifest.json')
    
    # Get existing version if updating
    version = 1
    created_timestamp = datetime.now().astimezone().isoformat()
    
    if args.update and os.path.exists(manifest_path):
        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                existing = json.load(f)
                version = existing.get('meta', {}).get('version', 0) + 1
                created_timestamp = existing.get('meta', {}).get('created', created_timestamp)
        except (IOError, json.JSONDecodeError):
            pass
    
    # Determine source: sidebar (default) or sitemap (explicit opt-in)
    if args.sitemap:
        # User explicitly requested sitemap (for obfuscated sidebars)
        sitemap_url = discover_sitemap(args.url)
        if sitemap_url:
            scraped_data = parse_sitemap(sitemap_url, args.url)
            source = "sitemap"
        else:
            print("Error: --sitemap flag provided but no sitemap found.", file=sys.stderr)
            sys.exit(1)
    else:
        # Default: use sidebar scraping
        if not args.selector:
            print("Error: --selector is required for sidebar scraping.", file=sys.stderr)
            print("Use --sitemap flag if the sidebar is obfuscated.", file=sys.stderr)
            sys.exit(1)
        scraped_data = scrape_links(args.url, args.selector)
        source = "sidebar"
    
    if not scraped_data:
        print(f"Error: No links found from {source}. Check the URL and selector.", file=sys.stderr)
        sys.exit(1)
    
    print(f"Found {len(scraped_data)} links from {source}")

    
    # Build manifest
    manifest = {
        "meta": {
            "id": args.id,
            "title": args.title,
            "url": args.url,
            "selector": args.selector,
            "section": args.section if args.section else None,
            "created": created_timestamp,
            "updated": datetime.now().astimezone().isoformat(),
            "version": version
        },
        "links": scraped_data
    }
    
    # Write manifest.json
    try:
        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        print(f"Manifest written to {manifest_path} ({len(scraped_data)} links)")
    except IOError as e:
        print(f"Error writing manifest: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
