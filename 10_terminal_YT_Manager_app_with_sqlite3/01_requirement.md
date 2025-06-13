# 📺 YouTube Manager - Terminal App (SQLite3-based)
````markdown

A command-line YouTube video manager built with Python. It supports adding, listing, updating, and deleting YouTube video entries using a local SQLite3 database.

---

## 🚀 Requirements

- Python 3.10+
- Packages:
  - `questionary` (for CLI menus)
  - `sqlite3` (standard library)
````



Install dependence:
```bash
pip install questionary
````




---
- sqlite3-document: https://docs.python.org/3/library/sqlite3.html

- Questionary-Link: https://pypi.org/project/questionary/

---

## 🎯 Client Requirements

1. Terminal-based YouTube video manager.
2. Store video info: title, URL, duration, description.
3. Save videos in a local database.
4. Provide options to:

   * List all videos
   * Add a new video
   * Update existing video info
   * Delete a video
   * Exit the app
5. Use a clean and interactive CLI menu.
6. Upgrade path to PostgreSQL support if needed.

---

## 🏗️ Development Guide

### 1. Database Setup

* Use SQLite3 for local DB.
* Create a `videos` table with the following schema:

```sql
CREATE TABLE IF NOT EXISTS videos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  url TEXT NOT NULL,
  duration TEXT NOT NULL,
  description TEXT NOT NULL
);
```

---

### 2. Functional Requirements

#### 📃 List All Videos

* Fetch and print all videos.
* Show total count.
* If no videos found, print “0 Video Found”.

#### ➕ Add New Video

* Prompt user to input `title`, `url`, `duration`, and `description`.
* Insert into the database using `INSERT INTO`.

#### ✏️ Update Existing Video

* Prompt for `video ID`.
* Fetch and display current values.
* Ask for new values; if left blank, keep the existing one.
* Run `UPDATE` query to apply changes.

#### ❌ Delete a Video

* Prompt for `video ID`.
* If found, confirm and delete it.
* If not found, show an error.

---

### 3. CLI Menu with Questionary

Use `questionary.select()` to show an interactive menu:

```
1. List favourite videos
2. Add a YouTube video
3. Update a YouTube video details
4. Delete a YouTube video
5. Exit
```

On selection:

* Run the appropriate function.
* Loop the menu until the user exits.

---

## 🔁 Loop & Exit Handling

* Use a `while True` loop in `main()` function.
* Break the loop only when user selects "Exit".
* Always close DB connection on exit.

---

## 🐘 PostgreSQL Migration (Optional)

To use PostgreSQL instead of SQLite:

1. Install:

   ```bash
   pip install psycopg2-binary
   ```

2. Change DB connection:

   ```python
   import psycopg2
   con = psycopg2.connect(
       dbname="yt_db",
       user="postgres",
       password="your_password",
       host="localhost",
       port="5432"
   )
   ```

3. Replace `?` placeholders with `%s` in all SQL queries.

4. Update `requirements.txt`:

   ```
   questionary
   psycopg2-binary
   ```

---

## ✅ To Run the App

```bash
python yt_manager.py
```

---

## 📂 Project Structure

```
yt_manager/
│
├── yt_manager.py         # Main app file
├── yt_manager.db         # SQLite DB file
└── requirements.txt      # Dependency list
```

---

## 🔚 Final Notes

* Works offline using SQLite.
* PostgreSQL-ready structure.
* Beginner-friendly CLI interface.
