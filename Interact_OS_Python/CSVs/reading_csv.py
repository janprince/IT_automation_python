import csv
#   python provides a module for working with csv files

"""
These files are stored in plaintext. And each line in a CSV file generally represents a single data record.
Each field in that record is separated by a comma, with the contents of the field stored between the commas.
"""

# first open the file
file = open("csv_file.txt")
csv_f = csv.reader(file)

for row in csv_f:
    name, tele, role = row  # num of variables on the left should = num of fields in a row of the csv
    print(f"Name: {name}, Phone: {tele}, Role: {role}")

file.close()