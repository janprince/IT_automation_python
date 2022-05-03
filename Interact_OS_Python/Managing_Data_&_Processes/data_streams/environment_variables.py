"""
 to access environment variables, we use the Environ dictionary provided by the OS module.
"""

import os

print(f"HOME: {os.environ.get('HOME', '')}" )
print(f"SHELL: {os.environ.get('SHELL', '')}" )
print(f"FRUIT: {os.environ.get('FRUIT', '')}" )