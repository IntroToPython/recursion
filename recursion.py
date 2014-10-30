import os
import os.path

def display_files_and_folders(path, indent = ""):
    for entry in os.listdir(path):
        print indent + entry
        new_path = os.path.join(path, entry)
        if os.path.isdir(new_path):
            display_files_and_folders(new_path, indent + "    ")

display_files_and_folders("examplepath")