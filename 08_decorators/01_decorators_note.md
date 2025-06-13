# Python Decorators A to Z (English + Bangla)

## 🧠 What is a Decorator?

A **decorator** is a function in Python that takes another function as an argument, adds some functionality, and returns it.

**Decorator একটি ফাংশন যা অন্য একটি ফাংশনকে আর্গুমেন্ট হিসেবে নেয় এবং তার মধ্যে অতিরিক্ত ফিচার যোগ করে।**

---

## 🎯 Why Use Decorators?

* Add functionality **without modifying the original function**
* Code becomes **cleaner and reusable**
* Useful for: logging, timing, caching, validation, authentication

**কেন ব্যবহার করব?**

* ফাংশনকে না বদলে নতুন ফিচার যোগ করা যায়
* কোড পরিষ্কার এবং পুনঃব্যবহারযোগ্য হয়

---

## 🧩 Basic Structure of a Decorator

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # কাজ করার আগে
        result = func(*args, **kwargs)
        # কাজ করার পরে
        return result
    return wrapper
```

**বাংলা ব্যাখ্যা:**

* `func` হলো আসল ফাংশন যেটিকে আমরা ডেকোরেট করছি
* `wrapper` হলো নতুন ফাংশন যেটি `func` এর কাজের আগে/পরে কিছু করে
* `*args` এবং `**kwargs` ফাংশনের সব ধরনের আর্গুমেন্ট নিতে পারে

---

## 🤔 Why Use Wrapper?

**Without wrapper:**

```python
def decorator(func):
    print("This won't work correctly!")
    return func
```

এইভাবে করলে আমরা `func` কে শুধু একবার কল করেই রিটার্ন করে দিচ্ছি। কিন্তু আগাম বা পরবর্তী কাজ করার সুযোগ নেই।

**With wrapper:** আমরা চাই ফাংশন কলের সময় কিছু ঘটুক, তাই `wrapper` দরকার:

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result
    return wrapper
```

---

## 🧪 Problem 1: Timing Function Execution

```python
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Executed in {end - start:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(2)
    print("Finished")

slow_function()
```

**বাংলা:**

* ফাংশন চলার সময়ের হিসাব রাখে
* `time.time()` দিয়ে শুরু এবং শেষ সময় নেই
* Wrapper ছাড়া সময় মাপা যেত না

---

## 🛠️ Problem 2: Debugging Function Calls

```python
def debug_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@debug_decorator
def add(a, b):
    return a + b

add(3, 5)
```

**বাংলা:**

* কোন ফাংশন কখন, কী দিয়ে কল হলো এবং কী রিটার্ন করল সেটা জানা যায়

---

## 🚀 Problem 3: Caching Return Values

```python
cache = {}

def cache_decorator(func):
    def wrapper(*args):
        if args in cache:
            print("Using cached result")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@cache_decorator
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))
```

**বাংলা:**

* আগের কলের রেজাল্ট মেমোরিতে রাখে
* পরে একই ইনপুট এলে সময় বাঁচে

---

## 🧵 Summary (সারাংশ)

* Decorators = ফাংশন + ফাংশনের উপর ফাংশন চালানো
* Wrapper দরকার যাতে ফাংশন চালানোর আগেও/পরে কাজ করা যায়
* `*args`, `**kwargs` ব্যবহার না করলে সব ধরনের ইনপুট নেওয়া সম্ভব নয়

---

## 📚 Bonus: Using `functools.wraps`

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

**wraps** ফাংশনের আসল নাম, ডকুমেন্টেশন, ইত্যাদি ঠিক রাখে। না হলে ডেকোরেটরের কারণে `func.__name__` ও `__doc__` হারিয়ে যায়।

---

## ✅ Practice Tips

* সবসময় ডেকোরেটর লিখে প্রিন্ট দিয়ে চেক করো
* debug, timing, logging, caching—সবই decorator দিয়ে সহজ
* বুঝতে wrapper কে `print(args, kwargs)` করে দেখো

---

## 📖 Useful Resources

* [Real Python: Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)
* Python Docs: `functools.wraps`

---

Happy Coding! 💻✨
