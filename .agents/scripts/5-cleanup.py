# 5-cleanup.py
import os
import shutil
import sys
import argparse


def main():
    """
    Cleans the build directory while preserving manifest.json.
    Deletes html/ and md/ subdirectories inside build/.
    """
    parser = argparse.ArgumentParser(description="Clean build artifacts from a project.")
    parser.add_argument("--project-dir", required=True, help="Path to the project directory.")
    args = parser.parse_args()

    build_dir = os.path.join(args.project_dir, 'build')
    html_dir = os.path.join(build_dir, 'html')
    md_dir = os.path.join(build_dir, 'md')

    cleaned = False

    # Remove html directory contents
    if os.path.exists(html_dir):
        try:
            shutil.rmtree(html_dir)
            os.makedirs(html_dir, exist_ok=True)
            print(f"Cleaned: {html_dir}")
            cleaned = True
        except OSError as e:
            print(f"Error cleaning {html_dir}: {e.strerror}", file=sys.stderr)

    # Remove md directory contents
    if os.path.exists(md_dir):
        try:
            shutil.rmtree(md_dir)
            os.makedirs(md_dir, exist_ok=True)
            print(f"Cleaned: {md_dir}")
            cleaned = True
        except OSError as e:
            print(f"Error cleaning {md_dir}: {e.strerror}", file=sys.stderr)

    if cleaned:
        print("Cleanup complete. manifest.json preserved.")
    else:
        print("Nothing to clean.")


if __name__ == "__main__":
    main()
