import csv
import sqlite3

import sqlalchemy
import redis


# exercise 1
books = [
    ["author", "book"],
    ["J R R Tolkien", "The Hobbit"],
    ["Lynne Truss", "Eats, Shoots & Leaves"],
]

with open("books.csv", "wt") as f:
    writer = csv.writer(f, lineterminator="\n")
    writer.writerows(books)

with open("books.csv", "rt") as f:
    reader = csv.DictReader(f)
    books = [row for row in reader]
    print(books)

with open("another_books.csv", "rt") as f:
    reader = csv.DictReader(f)
    books = [row for row in reader]
    print(books)

# exercise 2
sqlite_connection = sqlite3.connect("books.db")
cursor = sqlite_connection.cursor()
# cursor.execute(
#     """
#     CREATE TABLE books (
#     title VARCHAR(20) PRIMARY KEY,
#     author VARCHAR(50),
#     year INT)
#     """
# )

with open("another_books.csv", "rt") as f:
    reader = csv.DictReader(f)
    for row in reader:
        title = str(row["title"])
        author = str(row["author"])
        year = int(row["year"])
        cursor.execute(
            "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
            (title, author, year),
        )

cursor.execute("SELECT title FROM books ORDER BY title")
rows = cursor.fetchall()
print(rows)

cursor.execute("SELECT * FROM books ORDER BY year")
rows = cursor.fetchall()
print(rows)
cursor.close()
sqlite_connection.close()

# exercise 3
sqlalchemy_connection = sqlalchemy.create_engine("sqlite:///books.db")

with sqlalchemy_connection.connect() as conn:
    result = conn.execute(sqlalchemy.text("SELECT * FROM books ORDER BY year"))
    print(result.all())


# exercise 4
redis_connection = redis.Redis(host="localhost", port=6379, db=0)
redis_connection.hmset("test", {"count": 1, "name": "Fester Bestertester"})
redis_connection.hmget("test", 1)
redis_connection.hincrby("test", "count", 3)
