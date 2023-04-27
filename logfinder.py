import os
import subprocess
from pathlib import Path
import datetime
# set the file path to the folder you want to open
file_path = Path(r"C:\Users\nbdan\Documents\CodeStuff\Test")
search_string = 'FAILED'

# check if the folder exists
if os.path.exists(file_path):
    # open the folder using the Windows File Explorer command
    subprocess.Popen(f'explorer "{file_path}"')
    extension = ".txt" #The file extension you're searching fore
    failing_logs= [] #A list to neatly keep track of all the failing logs
    for file_with_extension in file_path.glob(f"*{extension}"):  # returns the file with extension or None
        with open(file_with_extension) as file:
            file_contents=file.read()
            # search for the string (search_string) in the file contents
            if search_string in file_contents:
                print(f"'{search_string}' found in {file_with_extension}")
                #print(file_with_extension) #prints the whole file path
                failing_logs.append(file_with_extension)
            #else:
                #print(f"'{search_string}' not found in {file_with_extension}")
    if failing_logs:
        for file in failing_logs:
            file_stat = file.stat()
            modified_date = datetime.datetime.fromtimestamp(file_stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            #print(file.name) # print the file name from the found_files list, but had the extension twice, ex. 'file1.txt.txt'
            print(f"{modified_date} : {file.stem}") # print the file name from the found_files list
            subprocess.run(["notepad.exe", file]) # open the file with the search_string in Notepad
    else:
        print(f"All logs are passing in: {file_path}")
else:
    print(f"Folder not found: {file_path}")
