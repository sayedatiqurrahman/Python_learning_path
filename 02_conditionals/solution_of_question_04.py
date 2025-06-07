# banana_color = input("Banana Colour is : ").lower()

banana_color_verity = {"yellow":"Ripe", "green":"Unripe", "brown":"Overripe"}

banana_color = "Green".lower()

if banana_color in banana_color_verity:
    print(f"Banana is {banana_color_verity[banana_color]}")
else:
    print("Banana colour is not recognized")





# Advance alternative way using select mode from the terminal 
import questionary # type: ignore

banana_color_question = questionary.select(
    "Banana Colour is : ",
    choices= list(banana_color_verity.keys()),# its an list of keys from the dictionary
    # choices=["yellow", "green", "brown"],
    # default="green"
).ask()

match banana_color_question:
    case "yellow":
        print("Banana is Ripe")
    case "green":
        print("Banana is Unripe")
    case "brown":
        print("Banana is Overripe")
    case _:
        print("Banana colour is not recognized")

# This code uses the questionary library to ask the user to select a banana color from a list of choices.
# The selected color is then matched against predefined cases to determine the ripeness of the banana.  
# If the selected color is not recognized, a default message is printed.
# Note: The questionary library is not a built-in Python library and needs to be installed separately.
# To install questionary, you can use pip:
# pip install questionary
# This code snippet demonstrates how to determine the ripeness of a banana based on its color.
# The banana color is checked against a predefined dictionary of colors and their corresponding ripeness states.
# If the color is recognized, it prints the ripeness state; otherwise, it indicates that the color is not recognized.
# The code also includes an advanced alternative using the questionary library to prompt the user for input.
# The banana color is then matched against predefined cases to determine the ripeness of the banana.
# The code uses a dictionary to map banana colors to their ripeness states.