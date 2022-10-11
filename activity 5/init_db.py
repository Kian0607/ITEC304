import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur= connection.cursor()

cur.execute("INSERT INTO post (title, content) VALUES (?, ?)",
    ('First Post', 'content for the first post' )
            )

cur.execute("INSERT INTO post (title, content) VALUES (?, ?)",
    ('Second Post', 'content for the second post' )
            )

connection.commit()
connection.close()