import re

log = "July 21 07:08:00 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"    # \d matches numeric characters and + means 'one or more occurance' of numeric characters
result = re.search(regex, log)
print(result)  # [12345]
print(result[1])  # 12345

result_2 = re.search(regex, "A completely different string that also has numbers [3456]")
print(result_2[1])  # 3456

result_3 = re.search(regex, "99 elephants in a [cage]")
print(result_3)  # None
#print(result_3[1])  # Error

print("\n------------------------------------------------")


# An efficient function
def extract_pid(log_line):
    pattern = r"\[(\d+)\]"
    match = re.search(pattern, log_line)
    if match is None:
        return ""
    else:
        return match[1]


print(extract_pid("99 elephants in a [cage]"))  # ""
print(extract_pid("i love numbers [23567]"))


print("-----------------------_---------------------------")
"""
Add to the regular expression used in the extract_pid function, to return the uppercase message in parenthesis, 
after the process id.
"""


def _extract_pid(log_line):
    regex = r"\[(\d+)\]: ([A-Z]*)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])


print(_extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(_extract_pid("99 elephants in a [cage]")) # None
print(_extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(_extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)