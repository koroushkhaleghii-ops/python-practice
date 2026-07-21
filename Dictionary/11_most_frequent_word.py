# Exercise 11: Find the most frequent word in a text

def most_frequent_manual(text):
    words = text.lower().split()
    if not words:
        return None
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    max_word = None
    max_count = -1
    for word, count in freq.items():
        if count > max_count:
            max_count = count
            max_word = word
    return (max_word, max_count)

# example
text = "Messi is the best footnall palyer in the world."
print(f"Text: {text}")
print("Using manual dict:", most_frequent_manual(text))