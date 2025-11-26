#!/usr/bin/env python3
import sys
import os
import shutil
from datetime import datetime

# --------------------------------------------------
# DEFAULT PATHS (used when no arguments are provided)
# --------------------------------------------------
DEFAULT_SOURCE = "/home/sowjanya/source"
DEFAULT_DEST = "/home/sowjanya/backup"


def unique_dest_path(dest_dir, filename):
    """
    Checks if the destination filename already exists.
    If yes → append timestamp to make it unique.
    """
    base, ext = os.path.splitext(filename)
    candidate = os.path.join(dest_dir, filename)

    # If no conflict → return original destination path
    if not os.path.exists(candidate):
        return candidate

    # If conflict → append timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_name = f"{base}_{timestamp}{ext}"

    return os.path.join(dest_dir, new_name)


def copy_all_files(source_dir, dest_dir):
    """
    Copy all files from source_dir → dest_dir.
    Create dest_dir if missing.
    Append timestamp for duplicate filenames.
    """
    # Validate source folder
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"❌ Source directory not found: {source_dir}")

    # Create destination folder if missing
    if not os.path.exists(dest_dir):
        print(f"📁 Destination missing. Creating: {dest_dir}")
        os.makedirs(dest_dir, exist_ok=True)

    entries = os.listdir(source_dir)

    if not entries:
        print("⚠ Source directory is empty. Nothing to copy.")
        return

    copied_count = 0

    for name in entries:
        src_path = os.path.join(source_dir, name)

        # Only copy files, not directories
        if not os.path.isfile(src_path):
            print(f"Skipping folder: {src_path}")
            continue

        dest_path = unique_dest_path(dest_dir, name)

        try:
            shutil.copy2(src_path, dest_path)
            print(f"✔ Copied: {src_path} → {dest_path}")
            copied_count += 1

        except PermissionError:
            print(f"❌ Permission denied: {src_path}")

        except Exception as e:
            print(f"❌ Failed to copy {src_path}: {e}")

    print(f"\n✅ Backup complete. Files copied: {copied_count}")


def main():
    """
    Determine which paths to use:
    - No args → use defaults
    - 2 args → use user-provided paths
    - Wrong usage → show help
    """

    # No arguments → use DEFAULT_SOURCE and DEFAULT_DEST
    if len(sys.argv) == 1:
        source = DEFAULT_SOURCE
        destination = DEFAULT_DEST

    # User provided source + destination
    elif len(sys.argv) == 3:
        source = sys.argv[1]
        destination = sys.argv[2]

    # Anything else → wrong usage
    else:
        print("\nUsage:")
        print("  python3 backup.py <source_dir> <destination_dir>")
        print("\nOr run without arguments to use:")
        print(f"  Source:      {DEFAULT_SOURCE}")
        print(f"  Destination: {DEFAULT_DEST}\n")
        sys.exit(1)

    try:
        copy_all_files(source, destination)

    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

    except Exception as e:
        print("❌ Unexpected error:", e)
        sys.exit(2)


if __name__ == "__main__":
    main()
