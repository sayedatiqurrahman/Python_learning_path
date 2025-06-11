
# 🌀 Recursive Function: Factorial Calculator in Python

## 📌 Problem

Create a **recursive function** to calculate the **factorial** of a number.

---

## ✅ What is Recursion?

**Recursion** is when a function **calls itself** to solve a smaller piece of the original problem.

> 🧠 A recursive function keeps calling itself with a **smaller input** until it reaches a **base case**, which stops the recursion.

---

## 🔢 What is Factorial?

The **factorial** of a number `n` is:


```

n! = n × (n-1) × (n-2) × ... × 1

```

### Example:
```

5! = 5 × 4 × 3 × 2 × 1 = 120

````

---

## 💡 Why Use Recursion?

- Solves **problems that are naturally recursive**, like tree traversal, factorial, Fibonacci, etc.
- Reduces **code complexity** for problems that can be broken into smaller subproblems.
- Often matches the **mathematical definition** closely.

---

## 🧪 Python Example: Factorial Function

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1  # 🛑 Base Case
    else:
        return n * factorial(n - 1)  # 🔁 Recursive Case

print(factorial(5))  # Output: 120
````

---

## 🔍 What Happens Behind the Scenes?

Calling `factorial(5)` works like this:

```
factorial(5) → 5 * factorial(4)
              → 5 * (4 * factorial(3))
                    → 5 * (4 * (3 * factorial(2)))
                          → 5 * (4 * (3 * (2 * factorial(1))))
                                → 5 * (4 * (3 * (2 * 1)))  ← base case reached
```

### Final result:

```
5 * 4 * 3 * 2 * 1 = 120
```

---

## ⚙️ Recursion Workflow Diagram

```
factorial(5)
   └── 5 * factorial(4)
         └── 4 * factorial(3)
               └── 3 * factorial(2)
                     └── 2 * factorial(1)
                           └── return 1 (base case)
```

Each call waits for the next to finish and multiplies the result.

---

## 🔐 Base Case vs Recursive Case

* **Base Case**: `n == 0 or n == 1` → returns 1 to stop recursion.
* **Recursive Case**: `n * factorial(n - 1)` → calls itself with a smaller number.

Without the base case, the function will keep calling itself forever → 🔁 **infinite recursion** → 💥 **RecursionError**.

---

## 🧠 When Not to Use Recursion?

* If recursion depth is too large → stack overflow.
* Iteration is often more efficient in memory for simple problems.

---

## ✅ Summary

| Term           | Meaning                                  |
| -------------- | ---------------------------------------- |
| Recursion      | A function calling itself                |
| Base Case      | Stops recursion                          |
| Recursive Case | Keeps recursion going with smaller input |
| Usefulness     | Breaks down problems like math/trees     |

---

## 🧩 Practice More

Try writing recursive versions of:

* Fibonacci sequence
* Sum of first `n` numbers
* Reverse a string

