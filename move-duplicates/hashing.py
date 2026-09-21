import hashlib
import os

def get_file_hash(filepath, chunk_size=8192, first_chunk_only=False):
    """
    Computes hash of a file.
    If first_chunk_only is True, reads only the first chunk (partial hash).
    """
    hasher = hashlib.md5()
    try:
        with open(filepath, "rb") as f:
            if first_chunk_only:
                chunk = f.read(chunk_size)
                if not chunk:
                    return None
                hasher.update(chunk)
            else:
                while chunk := f.read(chunk_size):
                    hasher.update(chunk)
        return hasher.hexdigest()
    except (PermissionError, OSError):
        return None

def get_duplicate_groups(source_folder):
    """
    Scans source_folder using a 3-tier approach:
    1. Group files by file size (instant metadata check).
    2. For matching sizes, group by 4KB partial hash.
    3. For matching partial hashes, group by full MD5 hash.
    
    Returns a dict mapping full_hash -> list of file paths (duplicates).
    """
    # Tier 1: Group by file size
    size_map = {}
    for root, _, files in os.walk(source_folder):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                # Skip empty files or unreadable files if desired
                size = os.path.getsize(filepath)
                size_map.setdefault(size, []).append(filepath)
            except (PermissionError, OSError):
                continue

    # Filter out sizes with only 1 file
    size_candidates = [paths for size, paths in size_map.items() if len(paths) > 1]

    # Tier 2: Group by partial hash (first 4KB)
    partial_map = {}
    for paths in size_candidates:
        for path in paths:
            p_hash = get_file_hash(path, chunk_size=4096, first_chunk_only=True)
            if p_hash is not None:
                partial_map.setdefault(p_hash, []).append(path)

    # Filter out partial hashes with only 1 file
    partial_candidates = [paths for p_hash, paths in partial_map.items() if len(paths) > 1]

    # Tier 3: Group by full hash
    full_map = {}
    for paths in partial_candidates:
        for path in paths:
            f_hash = get_file_hash(path, first_chunk_only=False)
            if f_hash is not None:
                full_map.setdefault(f_hash, []).append(path)

    # Return only hash groups that have duplicates (> 1 file)
    return {f_hash: paths for f_hash, paths in full_map.items() if len(paths) > 1}



        
