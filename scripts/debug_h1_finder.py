# debug_h1_finder.py
import os
import re

def find_h1_headings():
    """
    Reads the generated Markdown file and finds all lines that are H1 headings,
    checking for both ATX (#) and Setext (===) styles.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(os.path.dirname(script_dir))
    # Use the filename that was actually generated in the last run
    doc_path = os.path.join(project_dir, 'documents', 'opencode-ai-documentation.md')

    found_headings = []

    if not os.path.exists(doc_path):
        print(f"Error: Document not found at {doc_path}")
        print("Please run the 'new' command first to generate the document.")
        return

    with open(doc_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        # Check for ATX-style H1
        if re.match(r'^#\s+', line):
            found_headings.append(f"ATX Style H1 on Line {i + 1}: {line.strip()}")

        # Check for Setext-style H1
        # A line of 3 or more '=' characters makes the preceding non-blank line an H1
        if re.match(r'^[=]{3,}\s*$', line.strip()):
            if i > 0 and lines[i-1].strip(): # Check if there is a preceding non-blank line
                found_headings.append(f"Setext Style H1 on Line {i + 1}: The line above it ('{lines[i-1].strip()}') is the heading.")

    if found_headings:
        print("Found the following top-level (H1) headings:")
        for heading in found_headings:
            print(heading)
    else:
        print("No top-level (H1) headings (neither ATX nor Setext) were found.")

if __name__ == "__main__":
    find_h1_headings()
