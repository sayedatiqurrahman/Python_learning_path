

# 📦 Python Data Types

Python supports various built-in **data types** used to store different kinds of values. Here's a categorized list with examples and explanations:

---

## 🔢 Numbers

Python supports several numeric types:

* **Integer (`int`)**: Whole numbers
  `123`, `0`, `-99`

* **Float (`float`)**: Decimal numbers
  `3.14`, `-0.001`

* **Complex (`complex`)**: Numbers with a real and imaginary part
  `3 + 4j`

* **Binary (`bin`)**: Binary numbers
  `0b111` → `7`

* **Decimal** (from `decimal` module):
  `from decimal import Decimal`
  `Decimal('0.1') + Decimal('0.2')`

* **Fraction** (from `fractions` module):
  `from fractions import Fraction`
  `Fraction(1, 3) + Fraction(2, 3)  → 1`

---

## 🧵 String

Text values enclosed in `'` or `"`:

```python
username = 'Akbar'
```

### Examples

```python
len(username)         # 5
username[0]           # 'A'
username[-1]          # 'r'
username[2:5]         # 'bar'
```

* **Bytes**: `b'a\x01c'` → bytes string
* **Unicode**: `u'späm'` → Unicode string

🔧 `dir(username)` → Shows available string methods

---

## 📚 List

Mutable, ordered collection:

```python
my_list = [1, 'akbar', [4, 2, 2], 4.4]
list_from_range = list(range(5))  # [0, 1, 2, 3, 4]
```

---

## 🧱 Tuple

Immutable, ordered collection:

```python
my_tuple = ('Akbar', 1, 4, 'i')
tuple_from_str = tuple('atik')  # ('a', 't', 'i', 'k')
```

* `namedtuple` (from `collections`) allows tuple with named fields.

---

## 📖 Dictionary

Key-value pairs, unordered:

```python
my_dict = {'name': 'Atik', 'taste': 'yum'}
```

* `dict()` can be used to create dictionaries dynamically.

---

## 🔣 Set

Unordered, unique values:

```python
my_set = {'a', 'b', 'c'}
set_from_string = set('abc')  # {'a', 'b', 'c'}
```

---

## 📁 File

Represents a file object:

```python
file = open('eggs.txt')
binary_file = open(r'c:/ham.bin', 'wb')
```

---

## 🔘 Boolean

Logical values:

```python
is_active = True
is_deleted = False
```

---

## 🈳 None

Represents the absence of a value:

```python
result = None
```

---

## ⚙️ Function, Class, Module

Callable or reusable code structures:

* **Function**: Defined with `def`
* **Class**: Defined with `class`
* **Module**: Python file with reusable code (e.g., `math`, `datetime`)

```python
def greet(name):
    return f"Hello {name}"
```

---

## 🚀 Advanced Data Types

| Type            | Description                                     |
| --------------- | ----------------------------------------------- |
| **Iterator**    | Object that can be iterated one value at a time |
| **Generator**   | Functions using `yield`, lazy evaluation        |
| **Decorator**   | Wraps another function for extra behavior       |
| **MetaClasses** | Classes that define class behavior              |

---

## ✅ Summary Table

| Data Type      | Mutable | Ordered | Example              |
| -------------- | ------- | ------- | -------------------- |
| `int`, `float` | ❌       | N/A     | `123`, `3.14`        |
| `str`          | ❌       | ✅       | `'hello'`, `"world"` |
| `list`         | ✅       | ✅       | `[1, 2, 3]`          |
| `tuple`        | ❌       | ✅       | `(1, 2, 3)`          |
| `set`          | ✅       | ❌       | `{'a', 'b'}`         |
| `dict`         | ✅       | ❌       | `{'name': 'Atik'}`   |
| `bool`         | ❌       | N/A     | `True`, `False`      |
| `NoneType`     | ❌       | N/A     | `None`               |

---

