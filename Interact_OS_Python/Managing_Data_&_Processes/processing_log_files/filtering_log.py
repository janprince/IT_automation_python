"""
    Case Study:

The server that generates this log file has been acting strangely and we suspect it's due to a Cron job started by
one of the system administrators.

You may remember that Cron jobs are used to schedule scripts on UNIX-based operating systems.

To find out what's happening with the server, we want to audit the log files and see exactly who's been launching
CRON jobs. By looking at the sample log, we can see that the lines that'll be most interesting to us are the ones that
contain the Cron substring. These lines also show the user who started the Cron job wrapped in parentheses.
With this info, we can ignore any line without the Cron substring in it.
"""

# filtering log files with regex.
import re
import sys

logfile = sys.argv[1]    # a file as a parameter of our script

with open(logfile, 'r') as f:
    pattern = r'USER \((\w+)\)$'
    for line in f:
        if "CRON" not in line:
            continue
        result = re.search(pattern, line)
        print(result[1])


print("\n --------------------- Example 2 ------------------------------")
"""
We're using the same syslog, and we want to display the date, time, and process id that's inside the square brackets.
 We can read each line of the syslog and pass the contents to the show_time_of_pid function. 
 
 Fill in the gaps to extract the date, time, and process id from the passed line, 
 and return this format: Jul 6 14:01:23 pid:29440.
 
 Goal: Filter out the date and process id.
"""


def show_time_of_pid(line):
    date_pattern = r'\w+ \d (\d:?)+'
    date_result = re.search(date_pattern, line)

    pid_pattern = r'\[(\d+)\]'
    pid_result = re.search(pid_pattern, line)

    return f"{date_result[0]} pid: {pid_result[1]}"


with open(logfile, 'r') as f:
    for line in f:
        if "CRON" not in line:
            continue
        result = show_time_of_pid(line)
        print(result)