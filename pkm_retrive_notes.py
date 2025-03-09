import sqlite3

conn = sqlite3.connect('knowledge_management.db')
c = conn.cursor()

# Retrieve all notes
c.execute('SELECT * FROM notes')
for row in c.fetchall():
    print(row)
conn.close()

