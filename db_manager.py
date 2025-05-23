import sqlite3

def initialize_db():
    conn = sqlite3.connect('knowledge_management.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY,
                    date TEXT,
                    title TEXT,
                    content TEXT,
                    category TEXT,
                    tags TEXT
                )''')
    conn.commit()
    conn.close()

#def add_notes(notes):
#    existing_content = fetch_all_content()  # Get all existing content from the database
#    conn = sqlite3.connect('knowledge_management.db')
#    c = conn.cursor()
#
#    for note in notes:
#        if note[2] not in existing_content:  # Compare the "content" field of the note
#            c.execute('''INSERT INTO notes (date, title, content, category, tags)
#                         VALUES (?, ?, ?, ?, ?)''', note)
#        else:
#            print(f"Duplicate note found and skipped: {note[2]}")
#    conn.commit()
#    conn.close()

# def add_notes(notes):
#     conn = sqlite3.connect('knowledge_management.db')
#     c = conn.cursor()
#     for note in notes:
#         c.execute('''INSERT INTO notes (date, title, content, category, tags)
#                      VALUES (?, ?, ?, ?, ?)''', note)
#     conn.commit()
#     conn.close()

def add_notes(notes):
    # Fetch existing content from the database
    existing_content = fetch_all_content()  # A list of all "content" already in the database
    
    conn = sqlite3.connect('knowledge_management.db')
    c = conn.cursor()

    for note in notes:
        if note[2] not in existing_content:  # Compare the "content" field of the note
            c.execute('''INSERT INTO notes (date, title, content, category, tags)
                         VALUES (?, ?, ?, ?, ?)''', note)
        else:
            print(f"Skipped duplicate note: {note[2]}")
    conn.commit()
    conn.close()


def remove_note(note_id):
    conn = sqlite3.connect('knowledge_management.db')
    c = conn.cursor()
    c.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.commit()
    conn.close()

def replace_note(note_id, updated_note):
    conn = sqlite3.connect('knowledge_management.db')
    c = conn.cursor()
    c.execute('''UPDATE notes
                 SET date = ?, title = ?, content = ?, category = ?, tags = ?
                 WHERE id = ?''', (*updated_note, note_id))
    conn.commit()
    conn.close()


def fetch_all_content():
    conn = sqlite3.connect('knowledge_management.db')
    c = conn.cursor()
    c.execute('SELECT content FROM notes')  # Fetch only the "content" field
    existing_content = [row[0] for row in c.fetchall()]
    conn.close()
    return existing_content

def fetch_all_notes():
    conn = sqlite3.connect('knowledge_management.db')
    c = conn.cursor()
    c.execute('SELECT * FROM notes')
    notes = c.fetchall()
    conn.close()
    return notes

