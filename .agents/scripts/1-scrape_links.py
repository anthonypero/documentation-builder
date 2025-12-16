# 1-scrape_links.py
import argparse
import sys
import os
import csv
from urllib.parse import urljoin, urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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

    # Suppress webdriver-manager logs
    os.environ['WDM_LOG_LEVEL'] = '0'

    try:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        driver.get(url)
        
        # Wait for the navigation element to be present
        driver.implicitly_wait(10) # seconds
        
        nav_element = driver.find_element(By.CSS_SELECTOR, nav_selector)
        link_elements = nav_element.find_elements(By.TAG_NAME, "a")
        
        scraped_data = []
        unique_urls = set()
        
        base_url_parts = urlparse(url)

        for index, link_element in enumerate(link_elements):
            href = link_element.get_attribute('href')
            # Use get_attribute('textContent') which is more reliable for complex elements
            title = link_element.get_attribute('textContent').strip()

            if href:
                # Resolve relative URLs
                absolute_url = urljoin(url, href)

                # Remove fragments and query params for uniqueness check
                url_to_check = urljoin(absolute_url, urlparse(absolute_url).path)

                # Only add if it's a new, valid HTTP/HTTPS URL from the same domain
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
    parser.add_argument("--url", required=True, help="The URL to scrape.")
    parser.add_argument("--selector", required=True, help="The CSS selector for the navigation element.")
    
    args = parser.parse_args()
    
    scraped_data = scrape_links(args.url, args.selector)
    
    # Define CSV file path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(os.path.dirname(script_dir))
    build_dir = os.path.join(project_dir, 'build')
    csv_filepath = os.path.join(build_dir, 'links.csv')

    # Write to CSV
    if scraped_data:
        try:
            with open(csv_filepath, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['order', 'url', 'title', 'status', 'retry_count']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(scraped_data)
            # Output to stdout is no longer needed as the file is saved
        except IOError as e:
            print(f"Error writing to CSV file: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
