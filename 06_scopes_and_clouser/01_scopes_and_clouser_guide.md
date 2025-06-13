

# 🔍 Scopes and Closures in Python



## 1. What is Scope?

**Scope** refers to the region of a program where a variable is accessible.

---

## 2. Types of Variable Scope in Python

Python has four main scopes, often remembered by the acronym **LEGB**:

| Scope Level   | Description                                       | Example Location                         |
| ------------- | ------------------------------------------------- | ---------------------------------------- |
| **L**ocal     | Inside the current function                       | Variables defined inside a function      |
| **E**nclosing | Inside any enclosing functions (nested functions) | Variables in outer functions             |
| **G**lobal    | At the module level (file level)                  | Variables defined globally in the script |
| **B**uilt-in  | Predefined names in Python (like `len`, `print`)  | Python built-in functions and constants  |

---

## 3. Examples of Scope

### Local Scope

```python
def func():
    x = 10  # local variable
    print(x)

func()       # Output: 10
print(x)     # Error: x is not defined outside the function
```

---

### Global Scope

```python
x = 20  # global variable

def func():
    print(x)  # access global variable

func()      # Output: 20
print(x)    # Output: 20
```

---

### Modifying Global Variable Inside a Function

To modify a global variable inside a function, use the `global` keyword:

```python
x = 5

def func():
    global x
    x = 10

func()
print(x)   # Output: 10
```

---

### Enclosing (Nonlocal) Scope

Variables in an outer function can be accessed by nested inner functions.

```python
def outer():
    x = "hello"

    def inner():
        print(x)  # accessing enclosing variable

    inner()

outer()    # Output: hello
```

---

### Modifying Enclosing Variable: `nonlocal` Keyword

```python
def outer():
    x = 5

    def inner():
        nonlocal x
        x = 10
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()
```

**Output:**

```
Inner: 10
Outer: 10
```

---

## 4. What is a Closure?

A **closure** occurs when a nested function **remembers** the values from its enclosing scope even if the outer function has finished execution.

Closures are useful for data hiding and creating function factories.

---

### Example of Closure

```python
def outer(msg):
    def inner():
        print(msg)
    return inner

func = outer("Hello, Closure!")
func()  # Output: Hello, Closure!
```

Here, `inner()` remembers the value of `msg` from the `outer` function even after `outer` has finished.

---

### Why use Closures?

* To keep some data private.
* To generate customized functions.

---

## 5. Closure with State

```python
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

c = counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```

Here, `increment` keeps track of `count` using closure.

---

## 6. Summary Table

| Concept         | Description                            | Keyword              | Example                                 |
| --------------- | -------------------------------------- | -------------------- | --------------------------------------- |
| Local Scope     | Inside function variables              | None                 | `x = 10` inside `def func():`           |
| Global Scope    | Variables defined at top-level         | `global` to modify   | `global x` inside function              |
| Enclosing Scope | Variables in outer functions           | `nonlocal` to modify | Nested functions accessing outer vars   |
| Built-in Scope  | Python’s built-in names                | N/A                  | `len()`, `print()`                      |
| Closure         | Nested function remembering outer vars | N/A                  | Function returned from another function |

---

## 7. Tips

* Avoid excessive use of `global` to prevent bugs.
* Use closures to create cleaner, modular code.
* Understand scope to debug variable-related errors effectively.

---
