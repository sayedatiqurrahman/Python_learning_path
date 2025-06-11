### 🧪 **Encapsulation in OOP (বাংলায় ব্যাখ্যা)**

---

#### 🔐 **Encapsulation (সংবরণ)** কী?

**Encapsulation** মানে হলো কোনো object-এর ভেতরের ডেটা (Attribute) এবং ফাংশন (Method) — দুটোকে একসাথে **একটা প্যাকেট বা ক্লাসের মধ্যে বন্ধ করে রাখা**, যেন বাইরের কোনো ব্যবহারকারী (user) সরাসরি sensitive ডেটা access করতে না পারে।

---

#### 📦 সহজভাবে বুঝি

তুমি যখন একটা ওষুধের বোতল কিনো, তখন সেটার চারপাশে প্লাস্টিক বা ঢাকনা থাকে — যাতে কেউ সরাসরি ভিতরের কেমিক্যালে হাত দিতে না পারে।
একইভাবে **Encapsulation**-এ, sensitive data সরাসরি access না করে, শুধুমাত্র কিছু নির্দিষ্ট **method বা function** দিয়েই সেটাকে access করতে হয়।

---

#### 🔧 Python এ উদাহরণ

```python
class Student:
    def __init__(self, name, age):
        self.name = name              # public attribute
        self.__age = age              # private attribute (encapsulated)

    def get_age(self):
        return self.__age            # public method to access private data

    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
```

---

#### 🧾 ব্যাখ্যা

* `__age` হলো **private attribute**, মানে বাইরে থেকে সরাসরি `student.__age` দিয়ে access করা যাবে না।
* `get_age()` এবং `set_age()` হলো **getter এবং setter method** — এই method দিয়েই আমরা ডেটা দেখবো বা আপডেট করবো।
* এটা হলো **Encapsulation** — বাইরের user কে ডেটা access করতে দিলে হলেও, সে direct access না পেয়ে, নির্ধারিত method দিয়ে access করে।

---

#### 🎯 কেন Encapsulation দরকার?

✅ ডেটার নিরাপত্তা (data protection)
✅ কোডের structure clean থাকে
✅ ডেটার উপর কন্ট্রোল রাখা যায় (validation করা যায়)
✅ future maintenance সহজ হয়

---

#### 🧠 এক লাইনে সংজ্ঞা

> **Encapsulation** হলো এমন একটি প্রক্রিয়া যেখানে object-এর ডেটা এবং মেথড একত্রে রাখা হয় এবং ডেটার ওপর সরাসরি access সীমাবদ্ধ করে দেয়া হয়।

---

তুমি চাইলে আমি Getter/Setter নিয়ে আরও বিস্তারিত বা Advanced Level validation system দেখাতে পার Python-এ।
