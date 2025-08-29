import hashlib
import os

# =========================================
# Function: hashFile
# =========================================
# Generates an MD5 hash for a given file.
# Reads the file in chunks (64 KB) to handle large files efficiently.
def hashFile(fileName):
    hasher = hashlib.md5()       # Create MD5 hash object
    chunk_size = 65536           # 64 KB per chunk

    # Open the file in binary mode
    with open(fileName, 'rb') as file:
        buf = file.read(chunk_size)
        while buf:               # Continue until end of file
            hasher.update(buf)   # Update hash with current chunk
            buf = file.read(chunk_size)
    
    return hasher.hexdigest()    # Return final hash as a hexadecimal string


# =========================================
# Function: getAllFiles
# =========================================
# Recursively collects all files in the folder and its subfolders.
def getAllFiles(folderPath):
    allFiles = []
    for root, dirs, files in os.walk(folderPath):
        for file in files:
            fullPath = os.path.join(root, file)
            allFiles.append(fullPath)
    return allFiles


# =========================================
# Main Program
# =========================================
if __name__ == "__main__":
    hashMap = {}        # Dictionary to store unique file hashes
    duplicateFiles = [] # List to store paths of detected duplicates

    # Path to folder containing files
    filePath = r"D:\a"

    # Get all files recursively
    fileList = getAllFiles(filePath)

    # Check each file for duplicates
    for fullPath in fileList:
        key = hashFile(fullPath)      # Compute MD5 hash

        if key in hashMap:
            # Duplicate detected → add to list (without deleting)
            duplicateFiles.append(fullPath)
        else:
            # First occurrence of this hash → keep track
            hashMap[key] = fullPath

    # Print final report
    if duplicateFiles:
        print("Duplicate Files Detected (not deleted):")
        for file in duplicateFiles:
            print(file)
    else:
        print("No duplicate files found")