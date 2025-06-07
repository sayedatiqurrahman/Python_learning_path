# File Iteration Methods in Python

### Method 1: Using `__next__()` on file object

```python
f = open('filename.txt') # here is test_file.py
line = f.__next__()  # Get the next line
print(line)
f.close()
```
<br>
<br>


### Method 2: Using `readlines()` to read all lines at once

```python
lines = open('filename.txt').readlines()  # List of all lines
print(lines)

```
<br>
<br>


### Method 3: Using `next()` with file iterator

```python
line = next(open('filename.txt'))  # Get the first line
print(line)
```
