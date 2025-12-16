# Local Project Instructional Memory

## Project Goal & Architecture

The goal of this project is to create a command-line tool that scrapes web pages from a specified navigation element, converts their content into Markdown, and compiles them into a unified set of documents suitable for knowledge base creation (e.g., for NotebookLM).

### CLI Tool: `documentation`

The primary interface is a bash script named `documentation` located in `.agents/scripts/`. It orchestrates the entire process with support for multiple independent documentation projects.

**Commands:**

* `documentation new --url <url> --selector <nav_selector> --title <title> [--section <content_selector>] [--rate <seconds>]`
  * Creates a new documentation project.
  * `--url`: The entrypoint URL where the navigation is located.
  * `--selector`: The CSS selector for the navigation element containing the links to scrape.
  * `--title`: Human-readable title (required). Used to generate the project `id` (slugified).
  * `--section` (optional): A CSS selector for the main content area on each page.
  * `--rate` (optional): Cooldown period in seconds (default: 10).

* `documentation update [--id <id>]`
  * Re-scrapes and rebuilds an existing documentation project.
  * `--id`: The slugified project identifier. If omitted, uses the current directory (must contain `manifest.json`).

* `documentation cleanup [--id <id>]`
  * Removes build artifacts (html/md files) while preserving `manifest.json`.
  * `--id`: The slugified project identifier. If omitted, uses the current directory.

### Architecture: Modular Python Scripts

The `documentation` script executes a series of numbered Python scripts in a pipeline:

1. **`1-scrape_links.py`**: Scrapes links and creates/updates `manifest.json`.
2. **`2-download_pages.py`**: Downloads HTML for each link in the manifest.
3. **`3-convert_to_md.py`**: Converts downloaded HTML files to Markdown.
4. **`4-compile_docs.py`**: Generates TOC and combines Markdown files into final document.
5. **`5-cleanup.py`**: Cleans build artifacts while preserving manifest.

### Directory Structure

Each documentation project is self-contained in its own folder:

```text
${PROJECT_DIR}/documents/[id]/
├── [id].md                      # Final compiled markdown
├── manifest.json                # Meta + scraped links
└── build/
    ├── html/                    # Downloaded HTML pages
    ├── md/                      # Converted markdown snippets
    └── rate_limit_state.json    # Persistent backoff state
```

### manifest.json Format

```json
{
  "meta": {
    "id": "vite-guide",
    "title": "Vite Guide",
    "url": "https://vite.dev/guide",
    "selector": "nav.VPSidebar",
    "section": "main.VPDoc",
    "created": "2025-12-16T11:26:00-05:00",
    "updated": "2025-12-16T11:26:00-05:00",
    "version": 1
  },
  "links": [
    {"order": 0, "url": "...", "title": "...", "status": "pending", "retry_count": 0}
  ]
}
```

## Project Variables

Project variables are used throughout your instructional memory. When you encounter `${VARIABLE_NAME}` tokens in instructions or examples, replace them with the corresponding values defined below:

* **PROJECT_DIR** = `/Users/apero/Projects/documentation-builder`
* **WEB_ROOT** = `NULL`
* **REPO_DIR** = `${PROJECT_DIR}`
* **GITHUB** = `github-personal`

## Global Project Files

Please load the following files to your instructional memory and keep them in context:

@./.agents/global/modules/project-structure-manifest.md

### Project-Specific Files

Keep an updated file tree and file descriptions here.

## Global Memory Modules

Please load the following files to your instructional memory and keep them in context:

@./.agents/global/modules/global-rules.md
@./.agents/global/modules/memory-modules.md
@./.agents/global/modules/session-notes-rules.md
@./.agents/global/modules/github.md

## Project-Specific Memory Modules

Please load the following files to your instructional memory and keep them in context:

<!-- Project-specific modules go here -->

## Current Functionality

The script employs a **global, persistent exponential backoff strategy** to handle server-side rate limiting during the download process (`2-download_pages.py`).

### How it Works

* **Global Retry Counter:** Maintained across the download session and stored in `rate_limit_state.json`.
* **Adaptive Cooldown:** Exponential backoff on `429` errors: `min(MAX_COOLDOWN, BASE_COOLDOWN * (2 ** (global_retry_count - 1)))`.
* **Persistent Backoff:** The counter is never reset during a session, ensuring progressive cooldowns up to `MAX_COOLDOWN` (120 seconds).
