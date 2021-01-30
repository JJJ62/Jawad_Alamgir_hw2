print("Welcome to the leap year program. Once you enter a year I will check if it's a leap year or not \n")

exitstatus = int(0)
while exitstatus == int(0):
    year = input("Please enter the year you would like to check \n")
    if year.isdigit():
        exitstatus = 1
    else:
        print("INVALID INPUT!!! Please enter a valid integer\n")

if(int(year) % 4 == 0):
    if(int(year) % 100 == 0):
        if(int(year) % 400 == 0):
            print(year + " is a leap year\n")
        else:
            print(year + " is not a leap year\n")
    else:
        print(year + " is a leap year\n")
else:
    print(year + " is not a leap year\n")