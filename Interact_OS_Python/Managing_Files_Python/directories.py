import os
# Working with directories

# To get current working directory
print(os.getcwd())      # returns the current working dir

# To create a directory
# os.mkdir("new_dir")     # creates a new directory called "new_dir" in current dir.

# To change the current working directory
os.chdir("new_dir")
print(os.getcwd())

# To remove a dir
# os.rmdir("new_dir")   # removes dir only if its empty

