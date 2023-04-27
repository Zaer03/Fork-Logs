import os
import subprocess

# set the file path to the folder you want to open
folder_path = r"C:\Users\nbdan\Documents\CodeStuff\Test"

# check if the folder exists
if os.path.exists(folder_path):
    # open the folder using the Windows File Explorer command
    subprocess.Popen(f'explorer "{folder_path}"')
else:
    print(f"Folder not found: {folder_path}")