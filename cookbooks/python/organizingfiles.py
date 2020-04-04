# file operations instead of operating on files
import shutil, os

# copy file and folders with shutil.copy()

# moving and renaming files and folders with shutil.move()

# permanently deleting files and folders with os.unlink(), os.rmdir(), shutil.rmtree()

# safe deletes
import send2trash
# send files and folders to the send2trash with send2trash.send2trash()

# operate on zipfiles with zipfile.ZipFile()
import zipfile
# reading zipfiles with .namelist(), .getinfo(), .file_size, .compress_size, and then .close()

# extract from zip file with with .extractall(), .extract(), and then .close()

# create and add to zipfiles with zipfile.ZipFile(), .write(), then .close()
