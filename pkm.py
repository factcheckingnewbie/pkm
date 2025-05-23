import os
from db_manager import initialize_db, add_notes, fetch_all_content
from gui_manager import get_notes_from_file, prompt_for_notes
from library_manager import ensure_nltk_resources
from nltk.corpus import stopwords
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk import FreqDist

# Ensure libraries are available
nltk_data_path = '/home/ptr/Development/pkm/nltk_data'
ensure_nltk_resources(nltk_data_path)

# Initialize database
initialize_db()
from db_manager import fetch_all_notes
# Fetch and print all notes
all_notes = fetch_all_notes()
for note in all_notes:
    print(f"ID: {note[0]}, Date: {note[1]}, Title: {note[2]}, Content: {note[3]}, Category: {note[4]}, Tags: {note[5]}")

# Define the categorize_text function
def categorize_text(text):
    tokenizer = PunktSentenceTokenizer()
    sentences = tokenizer.tokenize(text)
    word_tokens = [word for sentence in sentences for word in sentence.split()]
    stop_words = set(stopwords.words('english'))
    filtered_text = [word.lower() for word in word_tokens if word.lower() not in stop_words]
    fdist = FreqDist(filtered_text)
    most_common_word = fdist.most_common(1)
    return most_common_word[0][0] if most_common_word else 'Uncategorized'
# Load or prompt for notes
notes = prompt_for_notes()

# Categorize and add notes
categorized_notes = [(date, title, content, categorize_text(content), tags) for date, title, content, _, tags in notes]
add_notes(categorized_notes)

