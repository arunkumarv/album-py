import os
import random
import string

the_folder = "/Users/akv/Personal"
#the_folder = "/Users/akv/Desktop/album-py/test"

s = string.ascii_lowercase

def randomString(length):
    c = ''.join(random.choice(s) for i in range(length))
    return c

def random_names(foler_path):
    for root, dirs, files in os.walk(the_folder):
        for file in files:
            filename, file_extension = os.path.splitext(file)
            source = root + '/' + file
            destination = root + '/' + randomString(10) + file_extension
            try:
                os.rename(source, destination)
            except PermissionError:
                print(source, destination)
