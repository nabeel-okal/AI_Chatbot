import sqlite3 as s3

DB_NAME = 'chatbot.db'

conn = s3.connect(DB_NAME)

c = conn.cursor()

# c.execute("""
# CREATE TABLE IF NOT EXISTS jokes (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     joke TEXT NOT NULL
#     )
# """)

# joke_text = "Why don’t scientists trust atoms? Because they make up everything!"
# c.execute('INSERT INTO jokes (joke) VALUES (?)', (joke_text,))

c.execute("SELECT * FROM jokes")

print(c.fetchone())

conn.commit()

conn.close()
