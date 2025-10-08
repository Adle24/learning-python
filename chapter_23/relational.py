import sqlite3


conn = sqlite3.connect("enterprise.db")
cursor = conn.cursor()
# cursor.execute(
#     """
#     CREATE TABLE zoo (
#         critter VARCHAR(20) PRIMARY KEY,
#         count INT,
#         damages FLOAT)
#     """
# )

cursor.execute("INSERT INTO zoo VALUES('duck', 5, 0.0)")
cursor.execute("INSERT INTO zoo VALUES('bear', 2, 1000.0)")

cursor.execute("SELECT * FROM zoo ORDER BY count DESC")
rows = cursor.fetchall()
print(rows)

cursor.close()
conn.close()
