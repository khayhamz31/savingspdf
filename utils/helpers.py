import os

def ensure_folder(folder_path):
    """Create folder if it doesn't exist."""
    os.makedirs(folder_path, exist_ok=True)

def safe_filename(filename):
    """Sanitize filenames for saving."""
    return "".join(c for c in filename if c.isalnum() or c in (' ', '.', '_')).rstrip()