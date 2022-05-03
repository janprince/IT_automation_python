import re

print("-------------------Example 1------------------------------")

"""
    For example, say you had a list of all the countries in the world and you want to check which of those 
    names start and end in a. What will the pattern look like?
"""

print(re.search(r"A.*a", "Argentina"))
# different country


print(re.search(r"A.*a", "Azerbaijan"))  # the pattern matches some part of the string (but that's wrong)
"""
    So while Azerbaijan doesn't finish with A, it does have an A in its name. So it matches our pattern. 
    We need to make our patterns stricter by adding the beginning of a line and end of a line characters.

    By adding a dollar sign to our pattern, we've made it clear that we only want to match lines that begin and end
    with the letter a. 
"""

print(re.search(r"^A.*a$", "Azerbaijan"))  # doesn't match anymore
# pattern starts with capital A and ends with a small a

print(re.search(r"^A.*a$", "Australia"))  # pattern matches


print("\n-------------------Example 2------------------------------")

"""
    Using regular expressions, we can also construct a pattern that would validate if the string is a valid variable 
    name in Python. 
    Do you remember what the rules were? It can contain any number of letters numbers or underscores, 
    but it can't start with a number.
"""
pattern = r"^[a-zA-Z_]\w*$"
print(re.search(pattern, "_this_is_a_valid_variable"))  # matches
print(re.search(pattern, "this isn't a valid variable"))    # None
print(re.search(pattern, "my_variable1"))   # matches
print(re.search(pattern, "2variable"))  # None

# Alternative pattern
pattern2 = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern2, "_this_is_a_valid_variable"))  # matches
print(re.search(pattern2, "this isn't a valid variable"))    # None
print(re.search(pattern2, "my_variable1"))   # matches
print(re.search(pattern2, "2variable"))  # None

"""
    NB: \w is equivalent to [a-zA-Z0-9_]
"""


print("\n----------------------- Example 3 ------------------------")
"""
    code to check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter,
    followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point. 
"""


def check_sentence(text):
    result = re.search(r"^[A-Z].*[.?!]$", text)
    return result != None


print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False  (doesn't start with an uppercase letter)
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True