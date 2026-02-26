import os

def get_file_size_gb(path):
    return os.path.getsize(path) / (1024**3)