# 3-convert_to_md.py
import argparse
import os
import sys
import re
from bs4 import BeautifulSoup, Comment
from markdownify import markdownify as md

def convert_html_to_md(html_filepath, output_dir, section_selector=None):
    """
    Converts an HTML file to Markdown, demoting headings by one level.
    """
    with open(html_filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Aggressive script and style removal
    html_content = re.sub(r'<script.*?</script>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<style.*?</style>', '', html_content, flags=re.DOTALL)

    soup = BeautifulSoup(html_content, 'html.parser')

    content_element = soup.select_one(section_selector) if section_selector else soup.find('body')
    if not content_element:
        print(f"Warning: Section selector '{section_selector}' not found in {html_filepath}. Using body.", file=sys.stderr)
        content_element = soup.find('body')
        if not content_element:
            print(f"Error: No content found in {html_filepath}. Skipping.", file=sys.stderr)
            return

    # Demote headings
    for i in range(6, 0, -1):
        for header in content_element.find_all(f'h{i}'):
            header.name = f'h{i+1}'

    for tag in content_element.find_all(['iframe', 'header', 'footer', 'nav']):
        tag.extract()
    for comment in content_element.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    def img_replacement(el):
        alt_text = el.get('alt', '').strip()
        return f"[Image: {alt_text}]" if alt_text else "[Image]"

    markdown_content = md(
        str(content_element),
        heading_style="ATX",
        bullets="-",
        code_language="auto",
        img_converter=img_replacement
    ).strip()
    
    # Get the original filename (e.g., 001-some-title.html)
    base_filename = os.path.basename(html_filepath)
    md_filename = base_filename.replace('.html', '.md')
    md_filepath = os.path.join(output_dir, md_filename)

    os.makedirs(output_dir, exist_ok=True)
    with open(md_filepath, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"Converted {html_filepath} to {md_filepath}")

def main():
    parser = argparse.ArgumentParser(description="Convert HTML files to Markdown snippets.")
    parser.add_argument("--section", help="Optional CSS selector for the main content section.", default=None)
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(os.path.dirname(script_dir))
    html_input_dir = os.path.join(project_dir, 'build', 'html')
    md_output_dir = os.path.join(project_dir, 'build', 'md')

    if not os.path.exists(html_input_dir):
        print(f"Error: HTML input directory '{html_input_dir}' not found.", file=sys.stderr)
        sys.exit(1)

    for filename in sorted(os.listdir(html_input_dir)):
        if filename.endswith(".html"):
            html_filepath = os.path.join(html_input_dir, filename)
            convert_html_to_md(html_filepath, md_output_dir, args.section)

if __name__ == "__main__":
    main()