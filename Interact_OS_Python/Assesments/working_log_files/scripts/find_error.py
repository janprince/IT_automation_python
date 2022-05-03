import sys
import os
import re


def search_error(log_file):
    error = input("What is the error: ")
    returned_errors = []

    with open(log_file, mode='r', encoding="UTF-8") as file:
        for log in file.readlines():
            error_patterns = ['error']
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
        file.close()
    return returned_errors


def file_output(errors):
    with open("../data/errors_found.log", 'w') as file:
        for err in errors:
            file.write(err)
        file.close()


if __name__ == "__main__":
    log_file = sys.argv[1]
    errors = search_error(log_file)
    file_output(errors)
    sys.exit(0)


search_error("../data/fishy.log")