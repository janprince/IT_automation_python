def to_seconds(hours, minutes, seconds):
    return (3600*hours) + (60*minutes) + seconds


print("Welcome to this time converter")

cont = 'y'

while cont.lower() == 'y':
    hours = int(input("Enter number of hours: "))
    minutes = int(input("Enter number of minutes: "))
    seconds = int(input("Enter number seconds: "))

    print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
    print()
    cont = input("Do you want to do another conversion? [y to continue]: ")

print("Goodbye")