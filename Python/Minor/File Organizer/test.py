import os
import shutil
from pathlib import Path

folder_path = "/Users/kaustubhsawant/Library/CloudStorage/OneDrive-Personal/Documents/Python_Advanced_Projects/projects/Python"

#for printing the files & folders inside the directory
for x in os.listdir(folder_path):
    print(x)

#for printing the files using a type of filter
for x in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, x)):
        print(x)

#checking the extension of a file
def get_file_extension(fl_name):
    return os.path.splitext(fl_name)[1].lower()

for x in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, x)):
        print(get_file_extension(x))
EXT_MAP = {"Text":['txt'],
           "Markdown":['md'],
           }

def organize_folder(x):
    other_folder=""
    for file in os.listdir(x):
        file_path = os.path.join(x,file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            moved = False
            for category, extensions in EXT_MAP.items():
                if ext in extensions:
                    dest_folder = os.path.join(x,category)
                    print("Moved file",file)
                    moved = True
                    break
            if not moved:
                other_folder = os.path.join(folder_path,"others")
            print(other_folder)


organize_folder("/Users/kaustubhsawant/Library/CloudStorage/OneDrive-Personal/Documents/Python_Advanced_Projects/projects/Python")