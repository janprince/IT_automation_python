import re

print(re.search(r".com", "welcome"))

# using escape character
print(re.search(r"\.com", "welcome"))  # None

print(re.search(r"\.com", "mydomain.com"))  # pattern matches .com

"""
    On top of this, Python also uses the backslash for a few special sequences that we can use to represent 
    predefined sets of characters. 
    For example, \w matches any alphanumeric character including letters, numbers, and underscores. 
    Let's check out a couple of examples.
"""

print(re.search(r"\w*", "This is an example"))  # pattern matches only "This" because \w does not match spaces
print(re.search(r"\w*", "And_this_is_another_example"))  # This pattern matches aplhanumeric chars and underscores.

"""
    There's also \d for matching digits, 
                \s for matching whitespace characters like space, tab or new line, 
                 \b for word boundaries and a few others. 
"""
