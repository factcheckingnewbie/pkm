import nltk
import os

def ensure_nltk_resources(nltk_data_path='/home/ptr/Development/pkm/nltk_data'):
    # Set the NLTK data path
    nltk.data.path.append(nltk_data_path)

    # Define the required resources
    required_resources = ['tokenizers/punkt', 'corpora/stopwords']

    # Check and download resources only if missing
    for resource in required_resources:
        try:
            nltk.data.find(resource)
            print(f"{resource.split('/')[-1]} found!")
        except LookupError:
            print(f"{resource.split('/')[-1]} not found. Downloading...")
            nltk.download(resource.split('/')[-1], download_dir=nltk_data_path)

