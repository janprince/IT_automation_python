import re       # regex module in python
"""

"""

result = re.search(r"aza", "plaza")
"""
We call the search function on the re module, and told it to use the pattern aza on the string plaza. 
We then stored the return value of that function in the result variable. 
The r at the beginning of the pattern indicates that this is a rawstring. 
This means that Python interpreter shouldn't try to interpret any special characters, and instead, should 
just pass the string to the function as is. In this example, there are no special characters. 
The rawstring and the normal string are exactly the same, but it's a good idea to always use rawstrings for 
regular expressions in Python.
"""

print(result)
print("--------------------------------------------------")

result_0 = re.search(r'aza', "bazaar")
print(result_0)

print("\n------------------- circumflex ---------------------------")

#   Using Special Characters

# circumflex
result_1 = re.search(r"^x", "xenon")
print(result_1)

print("\n----------------- dot wildcard --------------------------")

# dot wildcard
result_2 = re.search(r"p.ng", "penguin")        # The dot wildcard serves
print(result_2)

result_3 = re.search(r"p.ng", "clapping")
print(result_3)

result_4 = re.search(r"p.ng", "sponge")
print(result_4)

result_6 = re.search(r"p.ng", "Pangaea", re.IGNORECASE)     # match becomes case-insensitive
print(result_6)

"""
    In regular expressions, the period ( . , also called "dot") is the wildcard pattern which 
    matches any single character. 
    Combined with the asterisk operator . * it will match any number of any characters.
"""

print("\n----------------------- check_aei ---------------------------")


def check_aei (text):
    """
    checks if the text passed contains the vowels a, e and i, with exactly one occurrence of
    any other character in between.
    """
    result_5 = re.search(r"a.e.i", text)
    return result_5 != None


print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True