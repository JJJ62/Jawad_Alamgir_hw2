

print("Welcome to the leap year program. Once you enter a year I will check if it's a leap year or not \n")

year = input("Please enter the year you would like to check \n")

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

