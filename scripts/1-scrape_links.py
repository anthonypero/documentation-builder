# 1-scrape_links.py
import argparse
import sys
import os
import json
from datetime import datetime
from urllib.parse import urljoin, urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def slugify(text):
    """Converts a string into a URL-friendly slug."""
    if not text:
        return "untitled"
    import re
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    text = re.sub(r'[-\s]+', '-', text)
    return text


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
        link_elements = nav_element.find_elements(By.TAG_NAME, "a")
        
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
    parser = argparse.ArgumentParser(description="Scrape links from a webpage's navigation element.")
    parser.add_argument("--project-dir", required=True, help="Path to the project directory.")
    parser.add_argument("--url", required=True, help="The URL to scrape.")
    parser.add_argument("--selector", required=True, help="The CSS selector for the navigation element.")
    parser.add_argument("--title", required=True, help="Human-readable title for the documentation.")
    parser.add_argument("--id", required=True, help="Slugified ID for the project.")
    parser.add_argument("--section", default="", help="CSS selector for the main content section.")
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
    
    # Scrape links
    scraped_data = scrape_links(args.url, args.selector)
    
    if not scraped_data:
        print("Error: No links scraped. Check the URL and selector.", file=sys.stderr)
        sys.exit(1)
    
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
