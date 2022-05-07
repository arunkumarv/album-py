import hashlib
import os

the_folder = "/Users/akv/Personal"

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

for root, dirs, files in os.walk(the_folder):
    for file in files:
        source = root+'/'+file
        print(md5(source)+'\t'+source)
