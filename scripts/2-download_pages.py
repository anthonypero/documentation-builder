# 2-download_pages.py
import os
import sys
import re
import argparse
import time
import json
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


def download_page(driver, url, output_path, wait_selector=None):
    """
    Downloads the content of a single URL using Selenium and saves it to a file.
    Returns 'SUCCESS', 'RATE_LIMITED', or 'FAILED'.
    """
    try:
        driver.get(url)
        
        if wait_selector:
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, wait_selector))
                )
            except Exception:
                print(f"Warning: Timeout waiting for selector '{wait_selector}' on {url}", file=sys.stderr)
        else:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
        content = driver.page_source
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Successfully downloaded {url} to {output_path}")
        return 'SUCCESS'
        
    except Exception as e:
        print(f"Error downloading {url}: {e}", file=sys.stderr)
        return 'FAILED'


def setup_driver():
    """Sets up the Chrome WebDriver."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    os.environ['WDM_LOG_LEVEL'] = '0'
    
    try:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    except Exception as e:
        print(f"Failed to initialize WebDriver: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Download pages using Selenium.")
    parser.add_argument("--project-dir", required=True, help="Path to the project directory.")
    parser.add_argument("--rate", type=int, default=10, help="Cooldown period in seconds (unused but kept for compatibility).")
    parser.add_argument("--wait-selector", help="CSS selector to wait for before saving the page.", default=None)
    args = parser.parse_args()

    # File paths relative to project directory
    build_dir = os.path.join(args.project_dir, 'build')
    html_output_dir = os.path.join(build_dir, 'html')
    manifest_path = os.path.join(args.project_dir, 'manifest.json')

    os.makedirs(html_output_dir, exist_ok=True)

    if not os.path.exists(manifest_path):
        print(f"Error: manifest.json not found at {manifest_path}", file=sys.stderr)
        sys.exit(1)

    # Load manifest
    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest = json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error reading manifest: {e}", file=sys.stderr)
        sys.exit(1)

    links = manifest.get('links', [])
    if not links:
        print("Error: No links found in manifest.", file=sys.stderr)
        sys.exit(1)

    # Setup driver
    driver = setup_driver()

    # Main processing loop
    try:
        for i, link in enumerate(links):
            if link.get('status') == 'pending':
                order = int(link.get('order', 9999))
                url = link.get('url')
                title = link.get('title')

                if not url:
                    print(f"Skipping row {i+1} due to missing URL.", file=sys.stderr)
                    links[i]['status'] = 'failed'
                    continue
                
                order_padded = f"{order:03d}"
                slug = slugify(title)
                filename = f"{order_padded}-{slug}.html"
                output_path = os.path.join(html_output_dir, filename)
                
                download_status = download_page(driver, url, output_path, args.wait_selector)
                
                if download_status == 'SUCCESS':
                    links[i]['status'] = 'downloaded'
                else:
                    links[i]['status'] = 'failed'
                
                time.sleep(1)

                # Write back to manifest after each download
                try:
                    manifest['links'] = links
                    with open(manifest_path, 'w', encoding='utf-8') as f:
                        json.dump(manifest, f, indent=2, ensure_ascii=False)
                except IOError as e:
                    print(f"Error writing manifest: {e}", file=sys.stderr)

    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    finally:
        driver.quit()
        print("All processing complete.")


if __name__ == "__main__":
    main()