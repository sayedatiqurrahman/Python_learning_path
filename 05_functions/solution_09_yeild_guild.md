
---

# 🔄 Python `yield` & Generator Functions – Full Quick Guide

---

## 🅐 What is `yield`?

In Python, `yield` is a special keyword used **inside a function** to make it a **generator**.

Instead of **returning all values at once**, it **pauses** the function and **sends one value at a time**.

---

## 🅑 Why Do We Need `yield`?

* ✅ To **save memory** by not storing all values at once.
* ✅ To **pause and resume** a function's execution.
* ✅ To **work with large data** efficiently.
* ✅ To avoid using lists when only one item is needed at a time.

---

## 🅒 The Purpose of `yield`

* 📦 **Lazy evaluation** – values are produced only when needed.
* 🔁 **Efficient iteration** – especially useful in loops.
* 🚀 **Better performance** with large sequences or infinite data.

---

## 🅓 Basic Syntax

```python
def generator_function():
    yield value
```

---

## 🅔 Simple Example

```python
def count_up_to(max):
    num = 1
    while num <= max:
        yield num
        num += 1
```

Using it:

```python
for number in count_up_to(3):
    print(number)
# Output: 1, 2, 3
```

---

## 🅕 Difference Between `return` and `yield`

| Feature        | `return`                  | `yield`                  |
| -------------- | ------------------------- | ------------------------ |
| Stops function | ✅ Yes                     | ❌ No (pauses function)   |
| Memory usage   | High (returns everything) | Low (one item at a time) |
| Usage          | One-time result           | Continuous/lazy result   |

---

## 🅖 Behind the Scenes

When a function uses `yield`:

1. It becomes a **generator**.
2. Calling the function returns a **generator object**.
3. Each call to `next()` resumes from where it paused.

Example:

```python
def demo():
    yield 1
    yield 2

g = demo()
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # StopIteration
```

---

## 🅗 Real-World Use Case: Even Number Generator

### Normal Function

```python
def even_list(x):
    return [i for i in range(2, x+1, 2)]
```

### Generator Function

```python
def even_gen(x):
    for i in range(2, x + 1, 2):
        yield i
```

Usage:

```python
for num in even_gen(10):
    print(num)  # 2, 4, 6, 8, 10
```

Also:

```python
g = even_gen(10)
print(next(g))  # 2
print(next(g))  # 4
```

---

## 🅘 Flowchart

```
Function Called → Executes until `yield` → Returns value → Pauses → next() resumes → Repeats → StopIteration
```

---

## 🅙 Summary Table

| Concept          | Meaning                                       |
| ---------------- | --------------------------------------------- |
| `yield`          | Pauses function and returns value             |
| Generator        | Function that uses `yield`                    |
| Memory Efficient | Yes, it doesn't store all values in memory    |
| next()           | Resumes generator function from last pause    |
| for loop         | Internally calls `next()` until StopIteration |

---

## ✅ When to Use `yield`

* Reading large files
* Processing big datasets
* Creating infinite sequences
* Handling streams or APIs
* Delaying computations

---

## 🧠 Final Thoughts

> Use `yield` when you need to **generate values one by one**, especially when **performance or memory** is a concern.

It’s a **cleaner, faster, and more Pythonic** way to loop and generate data!

---

