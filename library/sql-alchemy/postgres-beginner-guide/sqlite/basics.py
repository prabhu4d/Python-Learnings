import sqlite3
from datetime import datetime

conn = sqlite3.connect('database.db')

# Creating a Table books (DDL)
conn.execute("""CREATE TABLE IF NOT EXISTS books (
                title TEXT,
                author TEXT,
                pages INTEGER,
                published INTEGER                
                )""")

# Adding values (DML)
values = ('Deep Learning',
          'Ian Goodfellow et al.',
          775,
          datetime(2016, 11, 18).timestamp())

conn.execute("""INSERT INTO books VALUES (?, ?, ?, ?)""", values)

# reading rows
r = conn.execute("""SELECT * FROM books""")
print(r.fetchall())