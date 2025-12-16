# 5-cleanup.py
import os
import shutil
import sys

def main():
    """
    Removes the build directory to clean up all intermediate files.
    """
    # Go up two directories from the current script's location to find the project root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(os.path.dirname(script_dir))
    build_dir = os.path.join(project_dir, 'build')

    if os.path.exists(build_dir):
        try:
            shutil.rmtree(build_dir)
            print(f"Successfully removed build directory: {build_dir}")
        except OSError as e:
            print(f"Error: {e.strerror} - {e.filename}", file=sys.stderr)
            sys.exit(1)
    else:
        print("Build directory not found. Nothing to clean.")

if __name__ == "__main__":
    main()
