import re


def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    return "{} {}".format(result[2], result[1])


"""
    Automatic tests are usually written alongside the code that we want to test. 
    What this means in practice is creating a separate Python file with the test. 
    The convention is to call the script with the same name of the module that it's testing and appending
     the suffix _test. So for our rearrange module, we'll create the rearrange_test.py file.
"""
