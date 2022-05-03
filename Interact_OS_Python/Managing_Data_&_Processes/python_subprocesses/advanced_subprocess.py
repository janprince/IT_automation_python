# Advanced subprocess management
# run this script in bash
"""
    The subprocess module offers a lot of extra options that we can use in our scripts.
"""

import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp", my_env["PATH"]])

result = subprocess.run(['myapp'], env=my_env)

"""
     This script is modifying the contents of the path environment variable by adding a directory to it. 
     We then call the myapp command with that modified variable. Doing it this way, the command will run in 
     the modified environment with the updated value of path. 
"""
