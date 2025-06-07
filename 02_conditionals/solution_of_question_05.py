weather = input("Enter the weather (sunny, rainy, snowy): ").strip().lower()

if weather == "sunny":
    print("It's a beautiful day! Let's go outside.")
elif weather == "rainy":
    print("Read a book!")
elif weather == "snowy":
    print("Time to build a snowman!")
else:
    print("Weather not recognized. Please enter sunny, rainy, or snowy.")

# This code checks the weather condition and prints a message accordingly.
# If the weather is sunny, it suggests going outside.