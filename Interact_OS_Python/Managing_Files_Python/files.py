# working with files
# we might want to rename files, delete them, or see more information abt a file

import os

# os.remove("new.txt") #  deletes a file called new.txt from the current directory.

# os.rename("path_to_old_file", "path_to_new_file")

# to check if a file exists
print(os.path.exists("spyder.txt"))

# to get the filesize of a file
print(os.path.getsize("spyder.txt")) # returns the file size in bytes

# get date which file was last modified
print(os.path.getmtime("spyder.txt")) # returns a timestamp. To format it properly,
import datetime
timestamp = os.path.getmtime("spyder.txt")
date = datetime.datetime.fromtimestamp(timestamp)
print(date)

# get the absolute path of a file
abs_path = os.path.abspath("spyder.txt")
print(abs_path)

