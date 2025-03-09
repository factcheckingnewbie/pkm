import os
import sqlite3

import nltk
nltk.data.path.append('/home/ptr/Development/pkm/nltk_data')
from nltk.corpus import stopwords
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk import FreqDist

tokenizer = PunktSentenceTokenizer()

nltk.download('punkt', download_dir='/home/ptr/Development/pkm/nltk_data')
nltk.download('stopwords', download_dir='/home/ptr/Development/pkm/nltk_data')
FreqDist

# Define the categorize_text function with the custom tokenizer
def categorize_text(text):
    # Explicitly load the Punkt tokenizer
    tokenizer = PunktSentenceTokenizer()

    # Tokenize sentences and then words
    sentences = tokenizer.tokenize(text)  # First, tokenize into sentences
    word_tokens = [word for sentence in sentences for word in sentence.split()]  # Split sentences into words manually

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_text = [word.lower() for word in word_tokens if word.lower() not in stop_words]

    # Find the most frequent word
    fdist = FreqDist(filtered_text)
    most_common_word = fdist.most_common(1)
    return most_common_word[0][0] if most_common_word else 'Uncategorized'
conn = sqlite3.connect('knowledge_management.db')
c = conn.cursor()

notes = [
    ("2025-03-03", "Python Script", "Learn how to write a simple Python script for automating tasks.", "", ""),
    ("2025-03-03", "AI Research", "Explore AI-driven technologies and their applications.", "", "")
]

for note in notes:
    content = note[2]
    category = categorize_text(content)
    c.execute('''INSERT INTO notes (date, title, content, category, tags)
                 VALUES (?, ?, ?, ?, ?)''', (note[0], note[1], note[2], category, ""))

conn.commit()
conn.close()

