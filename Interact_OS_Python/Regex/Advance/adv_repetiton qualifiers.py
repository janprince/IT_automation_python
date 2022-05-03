"""
Up to now, we've used the Star, Plus and question mark repetition qualifiers. What if we wanted a pattern that repeats
a specific number of times? This could happen if we're processing a line that we know has some specific data in a
column, or we know that we want a string of a specific length. In cases like those, we would manually write the
same pattern as many times as we need it. But it would be hard to read and hard to maintain. And that's why Python
also offers numeric repetition qualifiers. These are written between curly brackets and can be one or two numbers
specifying a range. For example, to match any string of exactly five letters, we can use an expression like this one
"""
import re


# to match any string of exactly five letters
print(re.search(r"[a-zA-Z]{5}", "a ghost town"))  # matches "ghost"
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))  # matches "scary"

# to find all that matches
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))  # ['scary', 'ghost', 'appea']

# more strict (we want full words that are 5 characters long) {n}
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))  # ['scary', 'ghost']

# to match a range of number of letters {n,n}, say 5-10 letters
print(re.findall(r"\w{5,10}", "I really like strawberries"))    # ['really', 'strawberri']

# to match a range of at least {n,}
print(re.findall(r"\w{5,}", "I really like strawberries"))  # 5 or more repetitions

# to match a range of at most {,n}
print(re.findall(r"s\w{,20}", "I really like strawberries"))  # 5 or more repetitions
