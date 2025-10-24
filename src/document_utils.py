import re

def clean_text(text):
    cleaned = re.sub(r'[^\w\s]', '', text)
    cleaned = re.sub(r'\s+', ' ', cleaned)
    return cleaned.strip()


def word_count(text):
    words = clean_text(text).split()
    return len(words)


def get_top_n_words(text, n=5):
    words = clean_text(text).lower().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]
