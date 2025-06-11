

# 🔄 Python Loops

Loops are used to repeat a block of code multiple times until a condition is met.

---

## 1. What is a Loop?

A **loop** allows you to run the same code repeatedly without rewriting it.

---

## 2. Types of Loops in Python

* `for` loop
* `while` loop

---

## 3. `for` Loop

Used to iterate over a sequence (like a list, tuple, string, or range).

### Basic syntax

```python
for item in sequence:
    # code block to run
```

### Example: Loop over a list

```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```

**Output:**

```
apple
banana
cherry
```

---

### Example: Loop over a range

```python
for i in range(5):  # 0 to 4
    print(i)
```

**Output:**

```
0
1
2
3
4
```

---

## 4. `while` Loop

Repeats as long as the condition is true.

### Basic syntax

```python
while condition:
    # code block to run
```

### Example

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**Output:**

```
0
1
2
3
4
```

---

## 5. Loop Control Statements

### `break`

Exits the loop immediately.

```python
for i in range(10):
    if i == 3:
        break
    print(i)
```

**Output:**

```
0
1
2
```

---

### `continue`

Skips the current iteration and moves to the next.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

**Output:**

```
0
1
3
4
```

---

### `else` with loops

Runs after the loop completes normally (no `break`).

```python
for i in range(3):
    print(i)
else:
    print("Loop completed without break")
```

**Output:**

```
0
1
2
Loop completed without break
```

---

## 6. Nested Loops

Loops inside loops.

```python
for i in range(1, 4):
    for j in range(1, 3):
        print(f'i={i}, j={j}')
```

**Output:**

```
i=1, j=1
i=1, j=2
i=2, j=1
i=2, j=2
i=3, j=1
i=3, j=2
```

---

## 7. Practical Scenarios

### Scenario 1: Sum of numbers 1 to 10

```python
total = 0
for num in range(1, 11):
    total += num
print("Sum:", total)
```

---

### Scenario 2: Print even numbers using `while`

```python
num = 2
while num <= 10:
    print(num)
    num += 2
```

---

### Scenario 3: Find first number divisible by 7 between 1 and 20

```python
for i in range(1, 21):
    if i % 7 == 0:
        print("First divisible by 7:", i)
        break
```

---

## 8. Tips

* Use `for` loops when you know how many times to iterate.
* Use `while` loops for conditional iteration (loop until a condition changes).
* Always update loop variables in `while` loops to avoid infinite loops.
* Use `break` and `continue` to control loop flow.

---

## 9. Summary Table

| Statement      | Description                    | Example                     |
| -------------- | ------------------------------ | --------------------------- |
| `for`          | Iterate over sequence          | `for i in range(5):`        |
| `while`        | Repeat while condition is true | `while x < 10:`             |
| `break`        | Exit the loop immediately      | `if i == 3: break`          |
| `continue`     | Skip current iteration         | `if i == 3: continue`       |
| `else` (loops) | Runs if no `break` in loop     | `for ... else ...`          |
| Nested loops   | Loops inside loops             | `for i in ... for j in ...` |

---
