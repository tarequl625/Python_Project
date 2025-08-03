#Python-OS-Module Functions
import os
#Important functions of the Python os module:
# 1.Handling the Current Working Directory
# 2.Creating a Directory
# 3.Listing out Files and Directories with Python
# 4.Deleting Directory or Files using Python
# 5.File Permissions and Metadata

# 1. Handling the Current Working Directory
path = os.getcwd()
print(path)

# Change to parent directory
# Get and print the new current directory
os.chdir('../')
new_path = os.getcwd()
print("After changing:", new_path)

# 2. Creating a Directory
#mkdir() create single directories
current_path = os.getcwd()
directory = "E"
path = os.path.join(current_path,directory)
os.mkdir(path)

#makedirs() Can create nested directories.
current_path = os.getcwd()
directory = "Esc"
path = os.path.join(current_path,directory)
os.makedirs(path)

# 3.Listing out Files and Directories with Python
list = os.listdir()
print(list)

# 4.Deleting Directory or Files using Python
#remove file
current_path = os.getcwd()
directory = "Escape"
path = os.path.join(current_path,directory)
os.remove(path)

#remove folder
current_path = os.getcwd()
directory = "Escape"
path = os.path.join(current_path,directory)
os.rmdir(path)

#rename folder or file name
current_path = os.getcwd()
path_old = os.path.join(current_path, "E")
path_new = os.path.join(current_path, "G")
os.rename(path_old,path_new)

#check file or folder exist or not
path = os.getcwd()
if os.path.exists(path)==True:
    print("True")