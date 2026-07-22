# Exercise 22: Create a word frequency dictionary from a sentence

from collections  import Counter

def sentence_word_freq_counter(sentence):
    words = sentence.lower().split()
    return dict(Counter(words))

def sentence_word_freq_manual(sentence):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# Example
sentence = "Hello i'm Kourosh and  i'm practicing Python .  "
print(f"Sentence: {sentence}")
print("Using Counter:", sentence_word_freq_counter(sentence))
print("Using manual dict:", sentence_word_freq_manual(sentence))