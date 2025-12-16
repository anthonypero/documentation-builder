# 4-compile_docs.py
import os
import sys
import re
import argparse
import html

DEFAULT_MAX_WORDS_PER_FILE = 450000

def slugify(text):
    if not text:
        return "untitled"
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    text = re.sub(r'[-\s]+', '-', text)
    return text

def clean_heading_text(text):
    cleaned = html.unescape(text) # More robust unescaping
    cleaned = re.sub(r'\[(.*?)\]\(.*\)', r'\1', cleaned).strip()
    return cleaned

def compile_docs(input_dir, output_dir, title):
    base_filename = slugify(title)
    
    # 1. Combine all markdown files
    all_content = []
    for md_file in sorted(os.listdir(input_dir)):
        if md_file.endswith('.md'):
            with open(os.path.join(input_dir, md_file), 'r', encoding='utf-8') as f:
                all_content.append(f.read())
    full_markdown = "\n\n---\n\n".join(all_content)

    # DEBUG: Check for rogue H1s before we add our own
    if re.search(r'^#\s+', full_markdown, re.MULTILINE):
        print("WARNING: H1 heading found in compiled content BEFORE main title was added.", file=sys.stderr)

    # 2. Generate TOC and Inject Anchors
    toc_lines = []
    seen_slugs = set()
    final_lines = []
    heading_regex = re.compile(r'^(#+)\s+(.*)')
    in_code_block = False

    for line in full_markdown.split('\n'):
        if line.strip() == '```':
            in_code_block = not in_code_block
        
        match = heading_regex.match(line)
        if match and not in_code_block:
            level = len(match.group(1))
            text = match.group(2).strip()
            cleaned_text = clean_heading_text(text)

            # Create a unique slug for this heading
            slug = slugify(cleaned_text)
            original_slug = slug
            counter = 1
            while slug in seen_slugs:
                slug = f"{original_slug}-{counter}"
                counter += 1
            seen_slugs.add(slug)
            
            # Add anchor
            final_lines.append(f'<a name="{slug}"></a>')

            # Add to TOC if it's H2 or H3
            if 2 <= level <= 3:
                indent = "  " * (level - 2)
                toc_lines.append(f"{indent}- [{cleaned_text}](#{slug})")
        
        final_lines.append(line)

    final_content = "\n".join(final_lines)
    
    # 3. Assemble and Save
    toc_section = "## Table of Contents\n\n" + "\n".join(toc_lines) + "\n\n"
    document_to_write = f"# {title}\n\n{toc_section}{final_content}"
    
    output_filepath = os.path.join(output_dir, f"{base_filename}.md")
    os.makedirs(output_dir, exist_ok=True)
    with open(output_filepath, 'w', encoding='utf-8') as f:
        f.write(document_to_write)
        
    print(f"Compiled documentation saved to {output_filepath}")

def main():
    parser = argparse.ArgumentParser(description="Compile Markdown files.")
    parser.add_argument("--title", required=True, help="The main title for the final document.")
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(os.path.dirname(script_dir))
    md_input_dir = os.path.join(project_dir, 'build', 'md')
    final_output_dir = os.path.join(project_dir, 'documents')

    if not os.path.exists(md_input_dir):
        print(f"Error: Markdown input directory '{md_input_dir}' not found.", file=sys.stderr)
        sys.exit(1)

    compile_docs(md_input_dir, final_output_dir, args.title)

if __name__ == "__main__":
    main()
