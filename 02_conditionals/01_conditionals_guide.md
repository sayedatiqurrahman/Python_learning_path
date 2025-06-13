
# 🟢 Python Conditionals

Conditionals allow your program to make decisions and execute different code blocks based on conditions.

---

## 1. What is a Conditional?

A **conditional statement** runs a block of code only if a certain condition is true.

---

## 2. Basic Syntax

```python
if condition:
    # code to run if condition is True
elif another_condition:
    # code to run if another_condition is True
else:
    # code to run if all above conditions are False
```

---

## 3. `if` Statement

Runs the block if the condition is true.

```python
age = 20
if age >= 18:
    print("You are an adult.")
```

**Output:**
`You are an adult.`

---

## 4. `if...else` Statement

Executes one block if the condition is true, otherwise another block.

```python
age = 15
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

**Output:**
`Minor`

---

## 5. `if...elif...else` Statement

Checks multiple conditions sequentially.

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")
```

**Output:**
`Grade B`

---

## 6. Nested Conditionals

Conditionals inside conditionals.

```python
age = 25
if age >= 18:
    if age < 21:
        print("Adult but below 21")
    else:
        print("Adult 21 or older")
else:
    print("Minor")
```

**Output:**
`Adult 21 or older`

---

## 7. Multiple Conditions with Logical Operators

* `and` (both must be true)
* `or` (either one true)
* `not` (negation)

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
```

**Output:**
`Entry allowed`

---

## 8. Conditional Expressions (Ternary Operator)

Short form of `if...else`

```python
age = 17
status = "Adult" if age >= 18 else "Minor"
print(status)
```

**Output:**
`Minor`

---

## 9. Practical Scenarios

### Scenario 1: Check Voting Eligibility

```python
def check_voting_eligibility(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"

print(check_voting_eligibility(20))  # Eligible to vote
print(check_voting_eligibility(16))  # Not eligible to vote
```

---

### Scenario 2: Password Validation

```python
password = "Secr3t!"

if len(password) >= 8:
    if any(char.isdigit() for char in password):
        print("Password is valid")
    else:
        print("Password must contain at least one digit")
else:
    print("Password too short")
```

---

### Scenario 3: Grading System

```python
def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

print(grade(85))  # B
print(grade(55))  # F
```

---

## 10. Tips

* Indentation is **critical** in Python. All code blocks inside conditionals must be indented consistently.
* Conditions can be any expression that returns `True` or `False`.
* Use `elif` to check multiple alternatives, instead of multiple nested `if` statements.
* Logical operators help combine multiple conditions.

---

## 11. Summary Table

| Statement         | Purpose                    | Example                 |
| ----------------- | -------------------------- | ----------------------- |
| `if`              | Runs if condition is true  | `if x > 0:`             |
| `else`            | Runs if condition is false | `else:`                 |
| `elif`            | Checks another condition   | `elif x == 0:`          |
| Logical operators | Combine conditions         | `and`, `or`, `not`      |
| Ternary Operator  | One-line conditional       | `a if condition else b` |

---


</br></br>

## --> Now open `problems.md` and solve the `problems`
