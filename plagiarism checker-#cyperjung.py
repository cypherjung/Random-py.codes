#checker
import string
from collections import Counter
import math

def preprocess_text(text):
    # Remove punctuation and convert text to lowercase
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    return text

def calculate_cosine_similarity(doc1, doc2):
    # Preprocess the documents
    doc1 = preprocess_text(doc1)
    doc2 = preprocess_text(doc2)

    # Create word frequency dictionaries for both documents
    word_freq1 = Counter(doc1.split())
    word_freq2 = Counter(doc2.split())

    # Calculate dot product
    dot_product = 0
    for word in word_freq1:
        if word in word_freq2:
            dot_product += word_freq1[word] * word_freq2[word]

    # Calculate magnitude of vectors
    mag1 = math.sqrt(sum(word_freq1[word] ** 2 for word in word_freq1))
    mag2 = math.sqrt(sum(word_freq2[word] ** 2 for word in word_freq2))

    # Calculate cosine similarity
    similarity = dot_product / (mag1 * mag2 + 1e-10)  # Add a small value to avoid division by zero

    return similarity

def check_plagiarism(doc1, doc2, threshold=0.9):
    similarity = calculate_cosine_similarity(doc1, doc2)
    if similarity >= threshold:
        print("Plagiarism detected!")
    else:
        print("No plagiarism detected.")

# Example usage
document1 = "This is the first document."
document2 = "This is the second document."
document3 = "This is the third document."

check_plagiarism(document1, document2)
check_plagiarism(document1, document3)
