year = int(input("Enter a year"))

if (year % 400) == 0 and (year % 4) == 0 or (year % 100) != 0:
    print("this is a leap year")
else:
    print("this is not a leap year")
