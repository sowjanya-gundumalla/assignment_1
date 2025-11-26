#!/usr/bin/env python3
import sys
import os
import shutil
from datetime import datetime

def unique_dest_path(dest_dir, filename):
    """
    If dest_dir/filename exists, return a new filename with a timestamp.
    Example: file.txt -> file_20250121_153210.txt
    """
    base, ext = os.path.splitext(filename)
    candidate = os.path.join(dest_dir, filename)
    
    if not os.path.exists(candidate):
        return candidate  # No conflict → safe to use
    
    # Conflict → append timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_name = f"{base}_{timestamp}{ext}"
    return os.path.join(dest_dir, new_name)

def copy_all_files(source_dir, dest_dir):
    """
    Copies all files from source_dir → dest_dir.
    Adds timestamp if filename already exists in destination.
    """
    
    # 1. Validate source directory
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"❌ Source directory not found: {source_dir}")

    # 2. Create destination folder if missing
    if not os.path.exists(dest_dir):
        print(f"📁 Destination folder missing. Creating: {dest_dir}")
        os.makedirs(dest_dir, exist_ok=True)

    files = os.listdir(source_dir)
    
    if not files:
        print("⚠ Source directory is empty. Nothing to copy.")
        return
    
    copied_count = 0

    for name in files:
        src_path = os.path.join(source_dir, name)

        # Only copy files (skip subdirectories)
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
    # Expect exactly 2 arguments: source + destination
    if len(sys.argv) != 3:
        print("\nUsage:")
        print("   python3 backup.py <source_dir> <destination_dir>\n")
        sys.exit(1)

    source = sys.argv[1]
    destination = sys.argv[2]

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
