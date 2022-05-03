"""
    A regular expression, also known as regex or regexp, is essentially a search query for text
    that's expressed by string pattern. When you run a search against a particular piece of text,
    anything that matches a regular expression pattern you specified, is returned as a result of the search.

    In other words, regular expressions allow us to search a text for strings matching a specific pattern.
    Knowing about regular expressions can be useful for anyone who needs to perform text processing.
"""
import re   # regular expressions module


log = "July 21 07:08:00 mycomputer bad_process[12345]: ERROR Performing package upgrade"

# extracting process_id
index = log.index("[")
id = log[index+1:index+6]   # this process is subject to errors as the length of the process_id might differ.
print(id)

print("------------------------------------------------------------------")

# Alternative way by using regex
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])


