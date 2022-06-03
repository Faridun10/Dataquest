# The goal is to list all files that are contained in a given folder (directly or indirectly).

# In this case, we want to list the following files (could be in another order):

# folder1/file1.txt
# folder1/file2.txt
# folder1/folder2/file3.txt
# folder1/folder2/folder3/file4.txt


import os

def list_files(current_path):
    # Base case
    if not os.path.isdir(current_path):
        print(current_path)
    else:
        # General case
        for name in os.listdir(current_path):
            file_path = os.path.join(current_path, name)
            list_files(file_path)
        

list_files("folder1")
