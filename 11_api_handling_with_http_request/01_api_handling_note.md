

# 🌐 Modern API Tutorial in Python: Learn to Fetch & Use APIs Like a Pro

Welcome to your **first hands-on API project** using Python! In this guide, you’ll learn how to interact with external APIs using Python, handle JSON responses, and build a simple program to fetch random user data.

---

## 🧠 What is an API?

> **API (Application Programming Interface)** is a set of rules that lets your app talk to another app or service — like getting data from GitHub, weather forecasts, or currency rates.

Think of an API as:
- 📞 A phone call to a data provider
- 📦 You send a request → 📤 You receive a response (usually JSON)

---

## 📌 Why Learn APIs?

- 💬 Build chatbot apps (e.g., Telegram, Discord bots)
- 📰 Pull real-time news/weather/stocks
- 🛍️ Create ecommerce integrations (Shopify, Stripe)
- 🎓 Learn fundamentals for working with AI models (OpenAI, Hugging Face, etc.)

---

## 🛠️ Tools You'll Need

| Tool         | Use                          |
|--------------|------------------------------|
| Python 3.6+  | Programming language         |
| `requests`   | To make HTTP API calls       |
| Terminal     | To run your Python scripts   |

### 📦 Install Required Package

```bash
pip install requests
````

---

## 🧪 Project Goal

We’ll build a simple Python script that fetches a **random fake user** (name, email, country) from a free API and prints it out.

---

## 💡 Free Open Source APIs You Can Practice With

| API Name        | Link                                                                                     | Use Case         |
| --------------- | ---------------------------------------------------------------------------------------- | ---------------- |
| Free API        | [https://freeapi.app](https://freeapi.app)                                               | Random user data |
| JSONPlaceholder | [https://jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com)             | Fake blog data   |
| GitHub API      | [https://api.github.com/users](https://api.github.com/users)                             | Dev profile data |
| OpenWeatherMap  | [https://openweathermap.org/api](https://openweathermap.org/api)                         | Weather info     |
| REST Countries  | [https://restcountries.com](https://restcountries.com)                                   | Country info     |
| Public APIs     | [https://github.com/public-apis/public-apis](https://github.com/public-apis/public-apis) | Huge API list 📚 |

---

## 🧑‍💻 Full Example: `fetch_user.py`

```python
import requests

def fetch_random_user():
    url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

    data = response.json()

    if "success" in data and data["success"] and "data" in data:
        user = data["data"]
        username = user["login"]["username"]
        email = user["email"]
        country = user["location"]["country"]
        return username, email, country
    else:
        raise Exception("Invalid API response format")

def main():
    try:
        username, email, country = fetch_random_user()
        print(f"👤 Username: {username}")
        print(f"📧 Email: {email}")
        print(f"🌍 Country: {country}")
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
```

---

## 🔍 How It Works (Step-by-Step)

1. ✅ **Send a GET request** to the API using `requests.get()`.
2. ✅ **Parse the JSON** response with `.json()`.
3. ✅ **Extract fields** like username, email, country.
4. ✅ **Display or use** the data in your app.

---

## 🛡️ Error Handling Best Practices

| Issue                       | How to Handle                                |
| --------------------------- | -------------------------------------------- |
| API down / bad URL          | Check `response.status_code`                 |
| Unexpected JSON format      | Use `if` checks and try-except               |
| Network error (no internet) | Catch `requests.exceptions.RequestException` |

### Example

```python
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as err:
    print("❌ Network or API error:", err)
```

---

## 📚 API Terms You Should Know

| Term        | Meaning                                                            |
| ----------- | ------------------------------------------------------------------ |
| Endpoint    | The URL to which you send the request (`/users`, `/weather`, etc.) |
| Request     | The action you send (GET, POST, etc.)                              |
| Response    | The reply you get (usually JSON)                                   |
| Status Code | A 3-digit HTTP result (200=OK, 404=Not Found, 500=Server Error)    |
| Header      | Meta-data like API keys, content type                              |
| Params      | Query values in URLs like `?page=2&limit=10`                       |

---

## 🧬 JSON Example (Response)

Here’s a sample API response you’ll work with:

```json
{
  "success": true,
  "data": {
    "login": { "username": "jeff.davis" },
    "email": "jeff.davis@example.com",
    "location": { "country": "United States" }
  }
}
```

---

## 🔁 Bonus: Loop for Multiple Users

```python
for i in range(5):
    u, e, c = fetch_random_user()
    print(f"{i+1}. {u} ({e}) from {c}")
```

---

## ⚡ Async API Calls (Advanced Idea)

You can use `aiohttp` or `httpx` for non-blocking API requests:

```python
import aiohttp
import asyncio

async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.github.com/users') as resp:
            data = await resp.json()
            print(data)

asyncio.run(fetch())
```

---

## 🧵 Next Steps & Advanced Ideas

* 🔐 Use APIs with authentication tokens (e.g. GitHub, OpenAI)
* 🌐 Try `POST` requests to send data
* ⏱️ Add delay/throttle to avoid rate limits
* ⚡ Use `httpx` or `aiohttp` for async API calls
* 🧰 Build a CLI app using `argparse` or `Typer`
* 🖥️ Show data in GUI with `Tkinter` or web with `Flask`

---

## 🗂️ Project Structure

```
random-user-api/
│
├── fetch_user.py         # Main script
├── requirements.txt      # Dependencies
└── README.md             # This guide
```

---

## 📦 `requirements.txt`

```txt
requests
```

Install with:

```bash
pip install -r requirements.txt
```

---

## ✅ Summary

✅ You now know:

* What APIs are and how they work 🔍
* How to make GET requests using Python
* How to parse JSON responses
* How to handle errors safely
* Where to find free APIs to practice
* Bonus: How to use async API tools like `aiohttp`

---

## 💬 Feedback & Contributions

Found this helpful? Want more advanced versions (like async, Flask API server, etc.)? Open an issue or suggest a change!

---

Happy coding! 🐍⚡
