while True:
    user_input = input("Enter a number (0 to 10): ")

    try:
        number = int(user_input)
        if 0 <= number <= 10:
            print(f"You entered: {number}")
            print("Thank you!")
            break
        else:
            print("Please enter a number between 0 and 10.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
