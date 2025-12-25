# Documentation Builder

A CLI tool that scrapes web documentation from navigation elements, converts pages to Markdown, and compiles them into a single unified document — perfect for creating knowledge bases or importing into tools like NotebookLM.

## Features

- **Scrape entire documentation sites** from a navigation element or sitemap
- **Sitemap discovery** for sites with obfuscated sidebars
- **Convert HTML to clean Markdown** with heading hierarchy preserved
- **Generate Table of Contents** automatically
- **Per-project organization** with independent build directories
- **Update support** to re-scrape and rebuild existing projects

## Requirements

- **Python 3.8+**
- **Google Chrome** (for headless scraping via Selenium)
- **Node.js** (for markdownlint-cli2)

### Python Dependencies

```text
selenium
webdriver-manager
beautifulsoup4
markdownify
```

### Node Dependencies

```text
markdownlint-cli2
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/anthonypero/documentation-builder.git
   cd documentation-builder
   ```

2. Create a virtual environment and install Python dependencies:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install selenium webdriver-manager beautifulsoup4 markdownify
   ```

3. Install markdownlint-cli2 globally:

   ```bash
   npm install -g markdownlint-cli2
   ```

4. Make the script executable (optional):

   ```bash
   chmod +x scripts/documentation
   ```

## Usage

### Create New Documentation

**Using sidebar navigation (default):**

```bash
scripts/documentation new \
  --url "https://example.com/docs/" \
  --selector "nav.sidebar" \
  --title "Example Docs" \
  --section "main.content"
```

**Using sitemap (for sites with obfuscated sidebars):**

```bash
scripts/documentation new \
  --url "https://example.com/docs/" \
  --title "Example Docs" \
  --sitemap \
  --section "article"
```

**Arguments:**

| Argument     | Required | Description                                       |
| ------------ | -------- | ------------------------------------------------- |
| `--url`      | Yes      | Entry URL containing the navigation               |
| `--selector` | *        | CSS selector for the nav element with doc links   |
| `--title`    | Yes      | Human-readable title (generates project ID)       |
| `--section`  | No       | CSS selector for main content area                |
| `--sitemap`  | *        | Use sitemap for URL discovery instead of sidebar  |
| `--rate`     | No       | Cooldown period in seconds (default: 10)          |

> **Note:** Either `--selector` or `--sitemap` is required. Use `--sitemap` when the sidebar is dynamically loaded or collapsed.

### Update Existing Documentation

Re-scrape and rebuild an existing project:

```bash
# By project ID
scripts/documentation update --id example-docs

# Or from inside the project folder
cd documents/example-docs
../../scripts/documentation update
```

### Clean Build Artifacts

Remove downloaded HTML and converted Markdown, but preserve the manifest:

```bash
scripts/documentation cleanup --id example-docs
```

## Output Structure

Each documentation project is created in `documents/[id]/`:

```text
documents/example-docs/
├── example-docs.md      # Final compiled document
├── manifest.json        # Project config + scraped links
└── build/
    ├── html/            # Downloaded HTML pages
    └── md/              # Converted Markdown snippets
```

## Finding the Right Selectors

Use your browser's Developer Tools to find CSS selectors:

1. Right-click the navigation menu → "Inspect"
2. Find the parent element containing all doc links (often `nav`, `aside`, or a sidebar `div`)
3. Copy its selector (e.g., `nav.VPSidebar`, `#sidebar`, `.docs-nav`)

For the `--section` argument, find the main content container to avoid scraping headers/footers.

### When to Use `--sitemap`

Use the `--sitemap` flag when:

- The sidebar is dynamically loaded or heavily collapsed
- Clicking to expand doesn't reveal all links in the DOM
- The site has a well-structured sitemap at `/sitemap.xml` or `/docs/sitemap.xml`

> **Note:** Sitemap mode returns URLs in alphabetical order, not reading order.

## License

MIT
