# file operations
import os

# write file paths with os.path.join()
print(os.path.join('usr','bin','spam'))

# get current working directory with os.getcwd()
print(os.getcwd())

# change directory with os.chdir()


# make new directory with os.makedirs()


# os.path module

# get file size and folder content with os.path.getsize() os.listdir()

# check path validity with os.path.exists() .isdir() or .isfile()

# open a file with open()

# read file with .read() or .readlines()

# write to files with .write



# shelve module to save variables to to binary shelf files
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

# save variables with pprint.pformat()
