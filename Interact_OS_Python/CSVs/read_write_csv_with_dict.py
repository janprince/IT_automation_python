import csv

# read as dictionary
f = open('software.csv')
reader = csv.DictReader(f)
for row in reader:
    print(row)

f.close()

# writing with dictionary
users = [
    {"name": "Sol Mansi", "username": "solm", "department": "IT Infrastructure"},
    {"name": "Lio Nelson", "username": "Lion", "department": "User Experience Researcher"},
    {"name": "Charlie Grey", "username": "greyc", "department": "Development"},
]

keys = ["name", "username", "department"]
with open("user_department.csv", 'w') as file:
    writer = csv.DictWriter(file, fieldnames=keys)
    writer.writeheader()        # creates the first line of the csv based on the keys we passed
    writer.writerows(users)
