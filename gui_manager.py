import os
from datetime import datetime

import os
from datetime import datetime

import os
from datetime import datetime

def get_notes_from_file(file_path='new_notes.txt'):
    notes = []
    try:
        # Attempt to read the file
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split('|')  # Format: date|title|content|category|tags
                if len(parts) == 5:
                    notes.append(tuple(parts))
    except FileNotFoundError:
        # Gracefully handle the case where the file does not exist
        print(f"File '{file_path}' not found. Skipping file processing.")
        return notes

    # Rename the file after reading notes
    if notes:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        renamed_file_path = f"imported_notes_{timestamp}.txt"
        try:
            os.rename(file_path, renamed_file_path)
            print(f"Imported notes file renamed to: {renamed_file_path}")
        except OSError as e:
            print(f"Error renaming file: {e}")
    else:
        print("No valid notes found in the file.")

    return notes

def prompt_for_notes():
    print("Enter notes manually (type 'done' to finish):")
    notes = []
    while True:
        date = input("Date (YYYY-MM-DD): ")
        if date.lower() == 'done':
            break
        title = input("Title: ")
        content = input("Content: ")
        category = input("Category (optional): ")
        tags = input("Tags (optional): ")
        notes.append((date, title, content, category, tags))
    return notes

