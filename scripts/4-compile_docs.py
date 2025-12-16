# 4-compile_docs.py
import os
import sys
import re
import argparse
import json
import html


def slugify(text):
    if not text:
        return "untitled"
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    text = re.sub(r'[-\s]+', '-', text)
    return text


def clean_heading_text(text):
    cleaned = html.unescape(text)
    cleaned = re.sub(r'\[(.*?)\]\(.*\)', r'\1', cleaned).strip()
    return cleaned


def compile_docs(project_dir):
    """Compile markdown files into a single document with TOC."""
    manifest_path = os.path.join(project_dir, 'manifest.json')
    md_input_dir = os.path.join(project_dir, 'build', 'md')
    
    # Read manifest for title and id
    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest = json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error reading manifest: {e}", file=sys.stderr)
        sys.exit(1)
    
    title = manifest.get('meta', {}).get('title', 'Documentation')
    doc_id = manifest.get('meta', {}).get('id', 'documentation')
    
    # Combine all markdown files
    all_content = []
    for md_file in sorted(os.listdir(md_input_dir)):
        if md_file.endswith('.md'):
            with open(os.path.join(md_input_dir, md_file), 'r', encoding='utf-8') as f:
                all_content.append(f.read())
    full_markdown = "\n\n---\n\n".join(all_content)

    # DEBUG: Check for rogue H1s
    if re.search(r'^#\s+', full_markdown, re.MULTILINE):
        print("WARNING: H1 heading found in compiled content BEFORE main title was added.", file=sys.stderr)

    # Generate TOC and Inject Anchors
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

            slug = slugify(cleaned_text)
            original_slug = slug
            counter = 1
            while slug in seen_slugs:
                slug = f"{original_slug}-{counter}"
                counter += 1
            seen_slugs.add(slug)
            
            final_lines.append(f'<a name="{slug}"></a>')

            if 2 <= level <= 3:
                indent = "  " * (level - 2)
                toc_lines.append(f"{indent}- [{cleaned_text}](#{slug})")
        
        final_lines.append(line)

    final_content = "\n".join(final_lines)
    
    toc_section = "## Table of Contents\n\n" + "\n".join(toc_lines) + "\n\n"
    document_to_write = f"# {title}\n\n{toc_section}{final_content}"
    
    # Write to project directory with id as filename
    output_filepath = os.path.join(project_dir, f"{doc_id}.md")
    with open(output_filepath, 'w', encoding='utf-8') as f:
        f.write(document_to_write)
        
    print(f"Compiled documentation saved to {output_filepath}")


def main():
    parser = argparse.ArgumentParser(description="Compile Markdown files.")
    parser.add_argument("--project-dir", required=True, help="Path to the project directory.")
    args = parser.parse_args()

    md_input_dir = os.path.join(args.project_dir, 'build', 'md')
    if not os.path.exists(md_input_dir):
        print(f"Error: Markdown input directory '{md_input_dir}' not found.", file=sys.stderr)
        sys.exit(1)

    compile_docs(args.project_dir)


if __name__ == "__main__":
    main()
