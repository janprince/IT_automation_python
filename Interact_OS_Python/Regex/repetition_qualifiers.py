import re

# Repeated matches
print("--------------------- Repeated matches ------------------------")
print(re.search(r"Py.*n", "Pygmalion"))
# In plain English, you could read this RegEx as match 'Py' followed by any number of other characters followed by 'n'.

print(re.search(r"Py.*n", "Python Programming"))
# the dot wildcard takes on a any number characters from y untill the last n

# If we only wanted our patterns match letters, we should have used the character class instead like this:
print(re.search(r"Py[a-z]*n", "Python Programming")) # our pattern only matches Python

#  zero times is also a possibility
print(re.search(r"Py[a-z]*n", "Pyn"))  # pattern matches 'Pyn'


print("\n------------------- + -----------------------")
# The + character

# The plus character matches one or more occurrences of the character that comes before it.
print(re.search(r"o+l+", "goldfish"))  # pattern matches and returns 'ol'
print(re.search(r"o+l+", "woolly"))  # pattern matches and returns 'ooll'
print(re.search(r"o+l+", "boil"))  # patterns returns None because a character appears between o an l
print(re.search(r"r+", "correction")) # 'rr'


print("\n------------------- ? -----------------------")
# The question mark symbol is yet another multiplier. It means either zero or one occurrence of the character before it.

print(re.search(r"p?each", "To each their own."))  # pattern matches 'each' because p is optional (1/0 occurrence)
print(re.search(r"p?each", "I like peaches"))  # pattern matches 'peach'
