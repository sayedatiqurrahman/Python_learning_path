import datetime


age =  int(input("Enter your age: "))
day = datetime.datetime.now().strftime('%A')
print(f"Today is: {day}")
# day = 'Wednesday'

price = 12 if age > 18 else 8

if day == 'Wednesday':
    price = price - 2
    print(f"The ticket price is: ${price}")
else:
    print(f"The ticket price is: ${price}")


# This code calculates the ticket price based on the user's age and the day of the week.
# It checks if the user is under 18 years old to set a base price of $12, otherwise it sets the price to $8.
# If the day is Wednesday, it applies a discount of $2 to the ticket price.
# The final ticket price is printed based on the conditions.
# The code uses a conditional expression to determine the initial price based on age.