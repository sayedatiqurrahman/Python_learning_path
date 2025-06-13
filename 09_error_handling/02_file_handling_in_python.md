# 📁 File Handling in Python 📁

File handling is a common task in programming, and it involves reading data from files and writing data to files. Python provides built-in functions and methods for file handling.

### Opening Files

The `open()` function is used to open files. It takes the file name as the first argument and the mode as the second argument.

```python
file = open("my_file.txt", "r")  # Open the file in read mode
file = open("my_file.txt", "w")  # Open the file in write mode (overwrites existing content)
file = open("my_file.txt", "a")  # Open the file in append mode (adds to the end of the file)
file = open("my_file.txt", "x")  # Open the file in exclusive creation mode (raises an error if the file exists)
file = open("my_file.txt", "rb") # Open the file in binary read mode
file = open("my_file.txt", "wb") # Open the file in binary write mode
```

### Reading Files

*   `read()`: Reads the entire file content as a string.
*   `readline()`: Reads a single line from the file.
*   `readlines()`: Reads all lines from the file and returns them as a list of strings.

```python
file = open("my_file.txt", "r")
content = file.read()
print(content)
file.close()

file = open("my_file.txt", "r")
line = file.readline()
print(line)
file.close()

file = open("my_file.txt", "r")
lines = file.readlines()
for line in lines:
    print(line)
file.close()
```

### Writing to Files

*   `write()`: Writes a string to the file.
*   `writelines()`: Writes a list of strings to the file.

```python
file = open("my_file.txt", "w")
file.write("Hello, world!\n")
file.close()

file = open("my_file.txt", "w")
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
file.writelines(lines)
file.close()
```

### Closing Files

It's important to close files after you're done with them to release the resources they're using. You can use the `close()` method to close a file.

```python
file = open("my_file.txt", "r")
# ... do something with the file ...
file.close()
```

### Using `with` Statement (Context Manager)

The `with` statement provides a more elegant and safer way to handle files. It automatically closes the file when the block of code is finished, even if an exception occurs.

```python
with open("my_file.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed here
```

## Error Handling in File Operations

File operations can raise various exceptions, such as `FileNotFoundError`, `IOError`, and `PermissionError`. It's important to handle these exceptions to prevent your program from crashing.

```python
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print(f"Error: File not found. {e}")
except IOError as e:
    print(f"Error: An I/O error occurred. {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
