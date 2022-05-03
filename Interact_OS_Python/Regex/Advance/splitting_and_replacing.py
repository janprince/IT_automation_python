"""
Up to now we've been using two functions from the RE module: search and find all.
There are actually a few more functions that can be really handy depending on what we're trying to do.
    One of these functions is called split.
"""

import re

print("------------------ Split ---------------------------")

result = re.split(r"[.?!]", "One sentence. Another one! And the last one?")
print(result)   # ['One sentence', ' Another one', ' And the last one', '']
"""
    Check out how we are not escaping the characters that we wrote inside the square brackets. T
    hat's because anything that's inside the square brackets is taking for the literal character and not for 
    its special meaning. Also see how the notation marks aren't present in the resulting list. 

        If we want our split list to include the elements that we're using to split the values we can 
        use capturing parentheses like this.
"""

result_1 = re.split(r"([.?!])", "One sentence. Another one! And the last one?")
print(result_1)  # ['One sentence', '.', ' Another one', '!', ' And the last one', '?', '']
""" This gave us both the sentences and notation marks as elements of a list. """


print("\n ----------------  Sub -------------------------------")
"""
    Another interesting function provided by the RE module is called sub. It's used for creating new strings by 
    substituting all or part of them for a different string, similar to the replace string method but using 
    regular expressions for both the matching and the replacing.
"""

pattern = r"[\w.%+-]+@[\w.-]+"     # NB: the '+' means one or more occurrence
reg = re.sub(pattern, "[REDACTED]", "Received an email for go_nuts95@my.example.com")
print(reg)   # Received an email for [REDACTED]

# another example
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))  # Ada Lovelace
# we use \2 to refer to the second captur group and \1, the first captured group.

