import random

def apply_watermark(text):
    words = text.split()
    if len(words) > 5:
        i = random.randint(0, len(words)-2)
        words[i] = words[i] + ""  # subtle token variation
    return " ".join(words)

def detect_watermark(text):
    return "" in text
