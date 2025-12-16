# 2-download_pages.py
import os
import sys
import csv
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
    """
    Converts a string into a URL-friendly slug.
    """
    if not text:
        return "untitled"
    # Replace special characters with a space
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    # Replace one or more spaces or dashes with a single dash
    text = re.sub(r'[-\s]+', '-', text)
    return text

def download_page(driver, url, output_path, wait_selector=None):
    """
    Downloads the content of a single URL using Selenium and saves it to a file.
    Returns 'SUCCESS', 'RATE_LIMITED', or 'FAILED'.
    """
    try:
        driver.get(url)
        
        # Check for rate limiting (429) title or content if visible
        # Note: Selenium doesn't easily expose HTTP status codes directly.
        # We rely on page content or redirection if the site handles it visibly.
        # For now, we assume successful load if no exception.
        
        if wait_selector:
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, wait_selector))
                )
            except Exception:
                # If content doesn't load in time, we still save what we have, 
                # but log a warning.
                print(f"Warning: Timeout waiting for selector '{wait_selector}' on {url}", file=sys.stderr)
        else:
            # Basic wait for body
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
        # Get page source after JS rendering
        content = driver.page_source
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Successfully downloaded {url} to {output_path}")
        return 'SUCCESS'
        
    except Exception as e:
        print(f"Error downloading {url}: {e}", file=sys.stderr)
        return 'FAILED'

def load_global_retry_count(state_file_path):
    """Loads the global retry count from the state file."""
    try:
        if os.path.exists(state_file_path):
            with open(state_file_path, 'r') as f:
                state = json.load(f)
                return state.get('global_retry_count', 0)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Warning: Could not read state file at {state_file_path}. Starting with retry count 0. Error: {e}", file=sys.stderr)
    return 0

def save_global_retry_count(state_file_path, count):
    """Saves the global retry count to the state file."""
    try:
        with open(state_file_path, 'w') as f:
            json.dump({'global_retry_count': count}, f)
    except IOError as e:
        print(f"Error: Could not write to state file at {state_file_path}. Error: {e}", file=sys.stderr)

def setup_driver():
    """Sets up the Chrome WebDriver."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Suppress webdriver-manager logs
    os.environ['WDM_LOG_LEVEL'] = '0'
    
    try:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    except Exception as e:
        print(f"Failed to initialize WebDriver: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """
    Reads a CSV file with 'order', 'url', 'title', and 'status' columns,
    and downloads each URL where the status is 'pending'.
    """
    # --- Argument Parsing ---
    parser = argparse.ArgumentParser(description="Download pages using Selenium.")
    parser.add_argument("--rate", type=int, default=10, help="The base cooldown period (unused in Selenium version but kept for compatibility).")
    parser.add_argument("--wait-selector", help="CSS selector to wait for before saving the page.", default=None)
    args = parser.parse_args()

    # --- File Paths ---
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(os.path.dirname(script_dir))
    build_dir = os.path.join(project_dir, 'build')
    html_output_dir = os.path.join(build_dir, 'html')
    csv_filepath = os.path.join(build_dir, 'links.csv')
    state_filepath = os.path.join(build_dir, 'rate_limit_state.json')

    os.makedirs(html_output_dir, exist_ok=True)

    if not os.path.exists(csv_filepath):
        print(f"Error: links.csv not found at {csv_filepath}", file=sys.stderr)
        sys.exit(1)

    # --- Load Data ---
    links = []
    try:
        with open(csv_filepath, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames
            if 'status' not in (fieldnames or []):
                print(f"Error: The CSV file must have a 'status' column.", file=sys.stderr)
                sys.exit(1)
            links = list(reader)
    except IOError as e:
        print(f"Error reading CSV file: {e}", file=sys.stderr)
        sys.exit(1)

    # --- Setup Driver ---
    driver = setup_driver()

    # --- Main Processing Loop ---
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
                
                # Simple sleep to be nice to the server, though Selenium is naturally slower
                time.sleep(1)

                # Write back to CSV periodically (or after every download to be safe)
                try:
                    with open(csv_filepath, 'w', newline='', encoding='utf-8') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(links)
                except IOError as e:
                    print(f"Error writing to CSV: {e}", file=sys.stderr)

    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    finally:
        driver.quit()
        print("All processing complete.")

if __name__ == "__main__":
    main()