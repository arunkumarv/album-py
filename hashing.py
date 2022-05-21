import hashlib
import os

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def get_hash_map_list(the_folder):
    hash_map_list = []
    for root, dirs, files in os.walk(the_folder):
        for file in files:
            source = root+'/'+file        
            hash_map_list.append(dict([
                ("source", source ),
                ("hash", md5(source))
            ]))
    return hash_map_list


        
