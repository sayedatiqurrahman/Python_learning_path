import datetime


# year = int(input("Enter a year to check if it is a leap year: "))
# year = 2024
year = datetime.datetime.now().year


isleapYear =(year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

if isleapYear:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")