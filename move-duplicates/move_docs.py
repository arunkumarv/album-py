import os
from text_detector import text_from_image

the_folder = ""
docs_folder = ""

for root, dirs, files in os.walk(the_folder):
        for file in files:
            content = text_from_image(file)
            if len(content) > 10:
                try:
                    os.rename(file, os.path.join(docs_folder, "") +  os.path.basename(file))
                except IsADirectoryError:
                    print("IsADirectoryError")

