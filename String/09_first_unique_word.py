# Exercise 9: Find the first word that appears exactly once in a sentence

from collections import Counter

def first_unique_counter(sentence):
    words = sentence.lower().split()
    if not words:
        return None
    freq = Counter(words)
    for word in words:
        if freq[word] == 1:
            return word
    return None

def first_unique_manual(sentence):
    words = sentence.lower().split()
    if not words:
        return None
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    for word in words:
        if freq[word] == 1:
            return word
    return None

# Example
sentence = "apple  potato banana apple orange banana grape bean  bean potato"
print(f"Sentence: {sentence}")
print("Using Counter:", first_unique_counter(sentence))
print("Using manual dict:", first_unique_manual(sentence))