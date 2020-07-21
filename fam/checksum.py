import os, hashlib
from datetime import datetime


def walk(pathname, watchname):
    hashes = []
    for dirpath, dirs, files in os.walk(pathname):	
        for filename in files:
            fname = os.path.join(dirpath,filename)
            hash = get_hash(fname)
            hashes.append((fname, hash, watchname, get_time()))
    return hashes


def get_hash(filename):
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()


def get_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')