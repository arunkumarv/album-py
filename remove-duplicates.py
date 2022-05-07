#!/usr/local/bin/python3

# This code workswith hashvalue file
# hashvalue has hash in first column and filepath in the second column.
# which is sorted out against first column so same hash values comes together
# File paths of duplicate hashes are moved to another folder - duplicate.
# I could save 16 gb with this procedure.

import re
import os

with open('duplicates') as my_file:
    lines = my_file.readlines()

prevLine = [None, None]
files_to_delete = list()

#create a folder manually
binPath = "/Users/akv/duplicates/"

for line in lines:
    line = re.split(r'\t+', line.strip('\n'))
    if prevLine[0] == line[0]:
        files_to_delete.append(line[1])
    else:
        prevLine = line

for f in files_to_delete:
    f_file = os.path.basename(f)
    new_f = binPath + f_file
    os.rename(f, new_f)

