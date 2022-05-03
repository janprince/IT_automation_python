"""
    Sometimes it's easier or faster to use a system command as part of our Python script to accomplish a task,
    or use some functionality that doesn't exist in the Python modules, neither built in or external.

    For these cases, Python provides a way to execute system commands in our scripts, using functions provided by
    the subprocess module.
"""
# running system commands from python scripts (external commands)
# from this script, we're running linux commands. Hence run this script only in bash.

"""
    The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, 
    and obtain their return codes. This module intends to replace several older modules and functions:
"""

import subprocess

print(subprocess.run(["date"]))
print(subprocess.run(["sleep", '2']))  # sleeps for 2 seconds

print("\n --------------------------")
result = subprocess.run(["ls", "this_file_exists_not"])
print(result.returncode)  # returns 2; which indicates an unsuccessful execution.


print("\n--------------------------------------")

# obtaining the output of a system command

result0 = subprocess.run(["host", "8.8.8.8"], capture_output=True)
"""
    If we use the capture output parameter and the command writes any output to standard output, 
    it will be stored in the stdout attribute of the completed process instance.
"""

print(result0.returncode)       # 0
print(result0.stdout)       # b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'  - an array of bytes
print(result0.stdout.decode().split())  # ['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']
# the decode method uses UTF-8 encoding.

print("\n ------------------------------------------")
"""
    If we use the capture output parameter and the command writes any output to standard error, 
    it will be stored in the stderr attribute of the completed process instance.
"""

result1 = subprocess.run(["rm", "some_file"], capture_output=True)
print(result1.returncode)  # 1
print(result1.stdout) # b''
print(result1.stderr) # b"rm: cannot remove 'some_file': No such file or directory\n"


"""
    We've now seen that we can execute system commands from Python and check whether they succeeded or failed.
     We've also seen how to capture the standard output and standard error streams so we can use their content 
     in our scripts. 
     
     These skills can be super useful when writing scripts that use system commands for some involved task and 
     letting our Python scripts cover a broader range of tasks. 
"""