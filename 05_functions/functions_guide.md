
# ⚙️ Python Functions

Functions are reusable blocks of code that perform a specific task. They help organize code, make it reusable, and improve readability.

---

## 1. What is a Function?

A **function** is a named block of code designed to perform a particular task and can be called multiple times.

---

## 2. Why Use Functions?

* Reusability: Write once, use multiple times.
* Organization: Break complex problems into smaller parts.
* Readability: Clear and understandable code.
* Maintainability: Easy to update and debug.

---

## 3. Function Syntax

```python
def function_name(parameters):
    # function body
    return value  # optional
```

* `def`: Keyword to define a function.
* `function_name`: Name of the function.
* `parameters`: Inputs (optional).
* `return`: Output (optional).

---

## 4. Defining and Calling a Function

### Example 1: Simple function without parameters

```python
def greet():
    print("Hello, World!")

greet()
```

**Output:**

```
Hello, World!
```

---

### Example 2: Function with parameters

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Akbar")
```

**Output:**

```
Hello, Akbar!
```

---

### Example 3: Function with return value

```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)
```

**Output:**

```
7
```

---

## 5. Function Parameters

### Positional Arguments

```python
def multiply(x, y):
    return x * y

print(multiply(5, 6))  # 30
```

### Default Arguments

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()        # Hello, Guest!
greet("Atik")  # Hello, Atik!
```

### Keyword Arguments

```python
def describe(name, age):
    print(f"{name} is {age} years old.")

describe(age=25, name="Akbar")
```

---

## 6. Variable-Length Arguments

### `*args` — Non-keyword variable arguments

```python
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4))  # 10
```

### `**kwargs` — Keyword variable arguments

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Atik", age=25)
```

---

## 7. Anonymous Functions (Lambda)

Short one-line functions.

```python
square = lambda x: x * x
print(square(5))  # 25
```

---

## 8. Docstrings (Function Documentation)

Explain what your function does.

```python
def greet(name):
    """
    Greets the person by name.
    :param name: String, name of the person.
    """
    print(f"Hello, {name}!")

help(greet)  # shows the docstring
```

---

## 9. Practical Scenarios

### Scenario 1: Check if a number is even or odd

```python
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(4))  # True
print(is_even(7))  # False
```

### Scenario 2: Calculate factorial using recursion

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120
```

### Scenario 3: Convert Celsius to Fahrenheit

```python
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(celsius_to_fahrenheit(30))  # 86.0
```

---

## 10. Tips

* Use descriptive function names.
* Keep functions focused on a single task.
* Use comments and docstrings to explain functions.
* Avoid side effects unless necessary (e.g., printing inside functions).
* Test functions individually.

---

## 11. Summary Table

| Feature            | Description                             | Example                    |
| ------------------ | --------------------------------------- | -------------------------- |
| Define Function    | Use `def` keyword                       | `def greet():`             |
| Call Function      | Use function name with parentheses      | `greet()`                  |
| Parameters         | Inputs to function                      | `def add(a, b):`           |
| Return Value       | Output from function                    | `return a + b`             |
| Default Parameters | Parameters with default values          | `def greet(name="Guest"):` |
| Variable Arguments | `*args`, `**kwargs` for flexible inputs | `def f(*args, **kwargs):`  |
| Lambda (Anonymous) | One-line functions                      | `lambda x: x * x`          |
| Docstrings         | Documentation inside triple quotes      | `"""Function info"""`      |

---
