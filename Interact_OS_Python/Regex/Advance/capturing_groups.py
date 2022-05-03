import re
"""
    Capturing groups are portions of the pattern that are enclosed in parentheses. 
    
    Let's say that we have a list of people's full names. These names are stored as last name, comma, first name.
    We want to turn this around and create a string that starts with the first name followed by the last name. 
    We can do this using a regular expression with capturing groups.
"""

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")      # has two capture groups
print(result)

print(result.groups())

# using indexes
print(result[0])    # Lovelace Ada
print(result[1])    # Lovelace
print(result[2])    # Ada

string = "{} {}".format(result[2], result[1])
print(string)


# function

def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    else:
        return f"{result[2]} {result[1]}"


print(rearrange_name("Jan, Prince"))
print(rearrange_name("Hopper, Grace M."))  # doesn't match


# improved function
def rearrange(name):
    match = re.search(r"^(\w*), ([\w \.]*)$", name)   # [\w \.] character class to match spaces and dots (\.) with \w(alphanum)
    if match is None:
        return name
    else:
        return f"{match[2]} {match[1]}"

print(rearrange("Hopper, Grace M."))