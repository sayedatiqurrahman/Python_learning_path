# MongoDB and PyMongo: A Beginner's Guide

This guide provides a simple and easy-to-understand introduction to MongoDB and PyMongo, covering the basics of installation, setup, and implementation.

## ❓ What is MongoDB? ❓

MongoDB is a popular NoSQL database that stores data in flexible, JSON-like documents. Unlike traditional relational databases, MongoDB doesn't require a predefined schema, making it ideal for handling unstructured or semi-structured data.

## 🐍 What is PyMongo? 🐍

PyMongo is the official Python driver for MongoDB. It allows you to interact with MongoDB databases from your Python applications.

## ⚙️ Installation ⚙️

### Installing MongoDB

It's important to note that you don't necessarily need to install MongoDB locally. You can also use MongoDB Atlas, a cloud database service, which eliminates the need for local installation.

1.  **Download MongoDB:** Visit the official MongoDB website ([https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)) and download the appropriate version for your operating system.
2.  **Install MongoDB:** Follow the installation instructions provided on the MongoDB website.
3.  **Set up Environment Variables:** Add the MongoDB `bin` directory to your system's PATH environment variable. This allows you to run MongoDB commands from any terminal window.

### Installing PyMongo

You can install PyMongo using pip:

```bash
pip install pymongo
```

## 🔗 Connecting to MongoDB 🔗

To connect to a MongoDB database using PyMongo, you need to create a MongoClient instance:

```python
from pymongo import MongoClient

# Connect to MongoDB (default host and port)
client = MongoClient()

# Connect to MongoDB on a specific host and port
# client = MongoClient('localhost', 27017)

# Connect to MongoDB using a connection string
# client = MongoClient('mongodb://user:password@localhost:27017/')
```

## 🗄️ Working with Databases 🗄️

### Getting a Database

To access a specific database, use the following syntax:

```python
db = client['mydatabase']  # Access the 'mydatabase' database
# db = client.mydatabase # alternative way to access the database
```

### Creating a Database

MongoDB creates a database when you first store data in it. You don't need to explicitly create a database beforehand.

## 📦 Working with Collections 📦

### Getting a Collection

A collection is a group of MongoDB documents. To access a collection, use the following syntax:

```python
collection = db['mycollection']  # Access the 'mycollection' collection
# collection = db.mycollection # alternative way
```

### Creating a Collection

Similar to databases, MongoDB creates a collection when you first store data in it.

## 📝 Working with Documents 📝

### Inserting Documents

To insert a single document into a collection, use the `insert_one()` method:

```python
document = {'name': 'John Doe', 'age': 30, 'city': 'New York'}
result = collection.insert_one(document)
print(f"Inserted document ID: {result.inserted_id}")
```

To insert multiple documents, use the `insert_many()` method:

```python
documents = [
    {'name': 'Jane Smith', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'Peter Jones', 'age': 40, 'city': 'Chicago'}
]
result = collection.insert_many(documents)
print(f"Inserted document IDs: {result.inserted_ids}")
```

### Finding Documents

To find documents in a collection, use the `find()` method:

```python
# Find all documents
for document in collection.find():
    print(document)

# Find documents matching a specific criteria
for document in collection.find({'city': 'New York'}):
    print(document)
```

You can also use query operators to perform more complex queries:

```python
# Find documents where age is greater than 30
for document in collection.find({'age': {'$gt': 30}}):
    print(document)
```

### Updating Documents

To update a document, use the `update_one()` or `update_many()` methods:

```python
# Update a single document
result = collection.update_one(
    {'name': 'John Doe'},
    {'$set': {'city': 'San Francisco'}}
)
print(f"Modified {result.modified_count} document(s)")

# Update multiple documents
result = collection.update_many(
    {'age': {'$gt': 30}},
    {'$inc': {'age': 1}}  # Increment age by 1
)
print(f"Modified {result.modified_count} document(s)")
```

### Deleting Documents

To delete a document, use the `delete_one()` or `delete_many()` methods:

```python
# Delete a single document
result = collection.delete_one({'name': 'John Doe'})
print(f"Deleted {result.deleted_count} document(s)")

# Delete multiple documents
result = collection.delete_many({'city': 'Chicago'})
print(f"Deleted {result.deleted_count} document(s)")
```

## 💡 Example Implementation 💡

Here's a simple example that demonstrates how to use PyMongo to interact with a MongoDB database:

```python
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# Insert a document
document = {'name': 'Alice', 'age': 28, 'city': 'London'}
result = collection.insert_one(document)
print(f"Inserted document ID: {result.inserted_id}")

# Find documents
for document in collection.find():
    print(document)

# Update a document
result = collection.update_one(
    {'name': 'Alice'},
    {'$set': {'city': 'Paris'}}
)
print(f"Modified {result.modified_count} document(s)")

# Delete a document
result = collection.delete_one({'name': 'Alice'})
print(f"Deleted {result.deleted_count} document(s)")

# Close the connection
client.close()
```

## 🚀 Project: Simple Task List 🚀

Create a basic task list application to practice using MongoDB and PyMongo.

**Requirements:**

*   Allow users to add tasks with a title. ➕
*   Allow users to view all tasks in the list. 📃
*   Allow users to mark tasks as complete. ✅
*   Allow users to remove tasks from the list. 🗑️

Store the task list data in a MongoDB database using PyMongo. This project will help you practice inserting, finding, updating, and deleting documents.

## 📚 Conclusion 📚

This guide provides a basic introduction to MongoDB and PyMongo. With this knowledge, you can start building Python applications that interact with MongoDB databases. Remember to consult the official MongoDB and PyMongo documentation for more advanced features and options.
