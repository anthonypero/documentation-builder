# Local Project Instructional Memory

## Project Goal & Architecture

The goal of this project is to create a command-line tool that scrapes web pages from a specified navigation element, converts their content into Markdown, and compiles them into a unified set of documents suitable for knowledge base creation (e.g., for NotebookLM).

### CLI Tool: `documentation`

The primary interface will be a bash script named `documentation` located in `.agents/scripts/`. It will be accessible as a CLI and will orchestrate the entire process.

**Commands:**

* `documentation new --url <url> --selector <nav_selector> [--section <content_selector>]`
  * This command initiates the scraping and building process.
  * `--url`: The entrypoint URL where the navigation is located.
  * `--selector`: The CSS selector for the navigation element containing the links to scrape.
  * `--section` (optional): A CSS selector for the main content area on each page. If provided, only this section will be converted to Markdown.

* `documentation cleanup`
  * This command removes all temporary files and directories created during the build process.

### Architecture: Modular Python Scripts

The `documentation` script will execute a series of numbered Python scripts in a pipeline, each responsible for a distinct task. This follows a modular approach for clarity and maintainability.

1. **`1-scrape_links.py`**: Scrapes links from the initial URL.
2. **`2-download_pages.py`**: Downloads the HTML for each scraped link.
3. **`3-convert_to_md.py`**: Converts the downloaded HTML files to individual Markdown files.
4. **`4-compile_docs.py`**: Generates a Table of Contents and combines the individual Markdown files into final documents.
5. **`5-cleanup.py`**: Provides the logic for the `cleanup` command.

### Directory Structure

* **Scripts**: All executable scripts (`documentation`, `1-scrape_links.py`, etc.) will reside in `.agents/scripts/`.
* **Temporary Files**: A `build/` directory will be created in the project root to store intermediate files (`build/html/` and `build/md/`).
* **Final Output**: The final, compiled Markdown documents will be saved in a `documents/` directory in the project root.

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

The script currently employs a robust **global, persistent exponential backoff strategy** to handle server-side rate limiting during the download process (`2-download_pages.py`). This ensures that documentation scraping can complete successfully even when faced with aggressive throttling from the target server.

### How it Works:
- **Global Retry Counter:** A single counter, `global_retry_count`, is maintained across the entire download session. This counter is stored persistently in a `rate_limit_state.json` file within the `build/` directory, allowing the process to resume correctly even if interrupted.
- **Adaptive Cooldown:**
  - The script proceeds at maximum download speed until it encounters a `429 Too Many Requests` error for *any* URL.
  - Upon a `429` error, the `global_retry_count` is incremented.
  - A cooldown period is calculated using the formula: `min(MAX_COOLDOWN, BASE_COOLDOWN * (2 ** (global_retry_count - 1)))`.
  - The script pauses for this calculated duration before attempting to download the problematic URL again.
- **Persistent Backoff:** The `global_retry_count` is **never reset** during the session, even after successful downloads. This means that if the server continues to throttle the process, the cooldown periods will progressively increase (e.g., 10s, 20s, 40s, 80s) until the `MAX_COOLDOWN` (currently 120 seconds) is reached and maintained.
- **Efficiency:** This strategy maximizes download speed when the server permits, and gracefully backs off only when necessary, ensuring eventual completion of all downloads.

## Next Steps

The project will be refactored from a single-use tool into a multi-project documentation management system. This involves significant changes to the directory structure, command-line interface, and the underlying scripts to support concurrent, independent documentation builds and an update mechanism.

### 1. New Project-Based Directory Structure

The single `build/` and `documents/` directories will be deprecated. Each documentation project will be self-contained within its own directory, created in the project root.

- **Root Folder:** `${PROJECT_DIR}/[document-title]/`

Inside this folder, the following files and directories will be created and maintained:
- `[document-title].md`: The final compiled Markdown document.
- `manifest.csv`: A permanent record of all links for the project, their status, and titles (renamed from `links.csv`).
- `meta.json`: A file storing the initial build parameters (`--url`, `--selector`, `--section`, `--title`) to enable future updates.
- `build/`: A project-specific directory for temporary files, containing:
  - `html/`: For downloaded HTML pages.
  - `md/`: For converted, individual Markdown files.
  - `rate_limit_state.json`: To store the persistent global retry counter for the download process.

### 2. `documentation` Script Command Refactoring

The main `documentation` script will be updated to manage this new project-based workflow.

#### `new` command
- The `--title` argument will now be mandatory, as it defines the name of the root project directory.
- The command will create the full project directory structure as outlined above, including the `meta.json` file.

#### `cleanup` command
The command will be updated with flags for more granular control:
- `--dir <title>`: Cleans only the `build/` folder for the specified project.
- `--dir-global`: Finds and deletes the `build/` folder from *every* documentation project in the root directory.
- **Default Behavior:** Without any flags, the command will do nothing to prevent accidental data loss.

#### New `update` command
A new subcommand will be introduced to keep documentation fresh.
- **Usage:** `documentation update --title <title>`
- **Functionality:**
  1. Reads the `meta.json` file in the specified project directory to retrieve the original `--url` and `--selector`.
  2. Re-scrapes the source URL to get a fresh list of links.
  3. Compares the new list against the existing `manifest.csv`.
  4. If any new links are discovered, it will update the `manifest.csv` and trigger a full, fresh rebuild of the entire documentation set for that project (i.e., re-downloading all pages).

### 3. Core Python Script Modifications

All numbered Python scripts (`1-scrape_links.py`, `2-download_pages.py`, etc.) will be refactored. They will need to accept a new argument (e.g., `--title` or `--path`) to ensure they operate within the correct project directory, reading from and writing to the correct `manifest.csv`, `build/`, and `meta.json` files. This removes all assumptions about a single, global `build/` directory.
