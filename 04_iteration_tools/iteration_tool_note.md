# Behind the Scenes of Python Loops (Quick Guide)

In Python, loops work by internally using **iterators** and two main built-in functions: `iter()` and `next()`. Any object that can return its elements one by one is called an **iterable**. Python converts an iterable into an **iterator** using `iter()`, and then repeatedly calls `next()` to fetch each element until exhausted.

---

## How `iter()` and `next()` Work

- `iter(iterable)` calls the iterable’s `__iter__()` method and returns an **iterator** object.
- `next(iterator)` calls the iterator’s `__next__()` method to get the next element.
- When there are no more elements, `next()` raises a `StopIteration` exception, signaling the end of the loop.

---

## Example: Manual Iteration

```python
nums = [10, 20, 30]

iterator = iter(nums)   # same as nums.__iter__()

print(next(iterator))   # 10, same as iterator.__next__()
print(next(iterator))   # 20
print(next(iterator))   # 30

# next(iterator) now raises StopIteration
```
<br>
<br>


## Example: Simulating a for Loop with iter() and next()

```python
data = [1, 2, 3]
it = iter(data)

while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break

__________________________
# output: 
# 1
# 2
# 3


```

<hr>

## Flowchart of Iteration Process

```
Iterable → __iter__() → Iterator → __next__() → element → repeat until StopIteration
```



## Summary Table


| Concept  | Description                                                     | Example                    |
| -------- | --------------------------------------------------------------- | -------------------------- |
| Iterable | Object that can return an iterator                              | `list`, `str`, `dict`      |
| Iterator | Object with `__next__()` method to fetch elements               | Result of `iter(iterable)` |
| `iter()` | Returns an iterator from an iterable                            | `iter([1, 2, 3])`          |
| `next()` | Returns next item from an iterator, raises StopIteration at end | `next(iterator)`           |






<br>
<br>
<br>

## How Python for Loop Uses Iteration Internally

```python
for item in iterable:
    # do something


# is internally equivalent to:

it = iter(iterable)
while True:
    try:
        item = next(it)
        # do something
    except StopIteration:
        break

```

<br>
<br>

## Key Points

- Every iterable implements `__iter__()` returning an iterator.

- Every iterator implements `__next__()` returning the next element or raising `StopIteration`.

- Python loops and comprehensions rely on this protocol under the hood.


<br>
<br>
<hr/>
<br>
<br>
<br>
<br>
<br>







# Python Comprehension (Quick Guide)

Python comprehensions are a concise way to create collections like lists, dictionaries, sets, and generators from iterable data.

---

## List Comprehension

**Syntax:**

```python
[expression for item in iterable if condition]
```

**Example:**

```python
evens = [x for x in range(10) if x % 2 == 0]
# Output: [0, 2, 4, 6, 8]
```

---

## Dictionary Comprehension

```python
squares = {x: x * x for x in range(4)}
# Output: {0: 0, 1: 1, 2: 4, 3: 9}
```

---

## Set Comprehension

```python
unique = {x for x in [1, 2, 2, 3]}
# Output: {1, 2, 3}
```

---

## Generator Expression

```python
gen = (x * x for x in range(3))
print(next(gen))
# Output: 0
```

---

## Flowchart (List Comprehension)

```
Iterable → for each item → [optional condition] → expression → add to list
```

---

## Summary Table

| Type         | Example Code                         |
|--------------|--------------------------------------|
| List         | `[x for x in range(5)]`              |
| Dictionary   | `{x: x*x for x in range(5)}`         |
| Set          | `{x for x in [1,2,2,3]}`             |
| Generator    | `(x for x in range(3))`              |

---
