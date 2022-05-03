import re
import sys

logfile = sys.argv[1]    # a file as a parameter of our script

# we want the number of times a username appears

with open(logfile, 'r') as f:
    usernames = {}
    pattern = r'USER \((\w+)\)$'
    for line in f:
        if "CRON" not in line:
            continue
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) +1     # sweet code.
    print(usernames)