file = open("youtube.txt", "w")

try:
    file.write("This is a test file for YouTube manager.")
    
finally:
    file.close()
    print("File closed successfully.")



with open("youtube.txt", "w") as file:
    file.write("This is a test file for YouTube manager with context manager. testing from second system.")