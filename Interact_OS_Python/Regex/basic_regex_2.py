import re
"""
    - We've seen by now how we can use a dot in our regular expressions as a special character that can
    match any character.
    - In the regex world, this is known as a wildcard because it can match more than one character.
    Using a dot is the broadest possible wildcard because it matches absolutely any character.

    - But what if we wanted something stricter, like checking if an answer given by a user contains a valid character,
    or finding all the usernames in a CSV file that start with a vowel?
    - We have to restrict our wildcards to a range of characters to do this.
    For this task we use another feature of regexes called character classes.
    
    Character classes are written inside square brackets and let us list the characters we want to match inside
    of those brackets.
"""

# Character Classes
# For example, say we want to match the word Python but allow for both lowercase or uppercase p.
print(re.search(r"[Pp]ython", "Python"))

# we can also define a range of characters we want to match using a dash
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "what a way to go"))   # None because "way" is preceded by a space and doesn't match the range we defined

print("-------------- More Examples ----------------")
# more examples
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))   # NB:whats in the square bracket is a-z A-Z 0-9
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))

print("-------------- Exclusion (Range) ----------------")

# Creating a search pattern that looks any characters that's not a letter
# [^a-zA-Z] means match anything exclude the characters a-z and A-Z
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))  # pattern match the first space in the sentence ' '


print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))   # the pattern match '.'
# because we added a space in the character class, the pattern ignores spaces

print("-------------- Multiple (OR) ----------------")
"""
    If we want to match either one expression or another, we can use the pipe symbol(|) to do that. 
    This lets us list alternative options that can get matched. 
"""

# For example, we could have an expression that matches either the word cat or the word dog, like this.
print(re.search(r"cat|dog", "I like cats"))
print(re.search(r"cat|dog", "I like dogs"))

print(re.search(r"cat|dog", "I like both dogs and cats."))
"""  
    In this string, we actually have two possible matches for our search. 
    But we only get the first one. That's the way the search function works. 
    If we want to get all possible matches, we can do that using the findall function, 
    which is also provided by the re module.
"""

print(re.findall(r"cat|dog", "I like both cats and dogs.")) # returns a list of the match strings: cat, dog

