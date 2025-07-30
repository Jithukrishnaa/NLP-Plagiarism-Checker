import os
from src.preprocess import clean_text
from src.vectorizer import get_vectors
from src.similarity import calculate_similarity

# Directory with assignment files
DATA_DIR = "data"

# Load all assignment files
assignments = {}
for filename in os.listdir(DATA_DIR):
    if filename.endswith(".txt"):
        with open(os.path.join(DATA_DIR, filename), 'r', encoding='utf-8') as file:
            assignments[filename] = file.read()

# Clean and vectorize
texts = [clean_text(text) for text in assignments.values()]
filenames = list(assignments.keys())

vectors = get_vectors(texts)

# Calculate pairwise similarity
print("\nPairwise Assignment Similarities:\n")
for i in range(len(filenames)):
    for j in range(i + 1, len(filenames)):
        sim = calculate_similarity(vectors[i], vectors[j])
        print(f"{filenames[i]} vs {filenames[j]}: {sim:.2f}% similarity")