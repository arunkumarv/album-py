import os
import shutil
from hashing import get_duplicate_groups
from file_utils import get_unique_destination_path

def move_duplicates(source_folder, destination_folder, dry_run=False):
    """
    Finds duplicate files in source_folder using a 3-tier algorithm
    and moves duplicates (keeping 1 original per hash group) to destination_folder.
    """
    if not dry_run and not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    print(f"Scanning '{source_folder}' for duplicates...")
    duplicate_groups = get_duplicate_groups(source_folder)

    if not duplicate_groups:
        print("No duplicate files found.")
        return

    total_duplicates = 0
    total_bytes_saved = 0

    print(f"\nFound {len(duplicate_groups)} group(s) of duplicate files.\n")

    for file_hash, file_list in duplicate_groups.items():
        original = file_list[0]
        duplicates = file_list[1:]
        
        print(f"Original: {original}")

        for dup_path in duplicates:
            total_duplicates += 1
            try:
                file_size = os.path.getsize(dup_path)
                total_bytes_saved += file_size
            except OSError:
                file_size = 0

            filename = os.path.basename(dup_path)

            if dry_run:
                print(f"  [DRY RUN] Would move duplicate: {dup_path} -> {os.path.join(destination_folder, filename)}")
            else:
                target_dest_path = get_unique_destination_path(destination_folder, filename)
                try:
                    shutil.move(dup_path, target_dest_path)
                    print(f"  [MOVED] {dup_path} -> {target_dest_path}")
                except Exception as e:
                    print(f"  [ERROR] Failed to move {dup_path}: {e}")

    mb_saved = total_bytes_saved / (1024 * 1024)
    action_str = "Identified" if dry_run else "Moved"
    print(f"\nSummary: {action_str} {total_duplicates} duplicate file(s) ({mb_saved:.2f} MB total).")