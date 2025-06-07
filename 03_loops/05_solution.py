input_str ="tweeter"

for char in input_str:
    count_of_char = input_str.count(char)
    if count_of_char < 2:
        print(f"'{char}' is first non-repeated character")
        exit()
