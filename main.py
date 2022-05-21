from file_utils import random_names
from hashing import get_hash_map_list
import os

the_folder = "./test"
delete_folder = "./duplicates"

if not os.path.exists(delete_folder):
    os.makedirs(delete_folder)

# random_names(the_folder)
hash_map_list = get_hash_map_list(the_folder)

grouped = {}
 
for item in hash_map_list:
    grouped.setdefault(item['hash'], []).append(item)
 
for item in grouped:
    for d in grouped[item][1:]:
        if os.path.isfile(d["source"]):
            try:
                os.rename(d["source"], os.path.join(delete_folder, "") +  os.path.basename(d["source"]))
            except IsADirectoryError:
                print("IsADirectoryError")