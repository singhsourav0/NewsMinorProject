import nltk
import numpy as np
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import json

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

def preprocess_text(text):
    """
    Tokenizes text into sentences and removes stopwords.
    """
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words("english"))

    processed_sentences = []
    for sent in sentences:
        words = word_tokenize(sent.lower())  # Convert to lowercase
        words = [word for word in words if word.isalnum() and word not in stop_words]
        processed_sentences.append(" ".join(words))

    return sentences, processed_sentences

def compute_sentence_scores(sentences):
    """
    Computes sentence similarity using TF-IDF and builds a similarity matrix.
    """
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)
    
    # Compute similarity matrix
    similarity_matrix = np.dot(tfidf_matrix, tfidf_matrix.T).toarray()
    
    return similarity_matrix

def generate_summary(text, num_sentences=5):
    """
    Generates a summary using TextRank algorithm.
    """
    original_sentences, processed_sentences = preprocess_text(text)
    
    if len(original_sentences) <= num_sentences:
        return text  # If text is short, return as is

    similarity_matrix = compute_sentence_scores(processed_sentences)

    # Create graph and compute PageRank
    sentence_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(sentence_graph)

    # Rank sentences based on PageRank scores
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(original_sentences)), reverse=True)

    # Select top-ranked sentences
    summary_sentences = [s[1] for s in ranked_sentences[:num_sentences]]
    
    return " ".join(summary_sentences)

# with open("news_output.json") as f:
#     data = json.load(f)

# for item in data[2:3]:
#     item["summary"] = generate_summary(item["article_text"])
#     print(item["headline"])
#     print(item["summary"])
#     print("-"*60)
#     print(item["article_text"])