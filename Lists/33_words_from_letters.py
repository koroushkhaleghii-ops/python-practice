# Exercise 33: Find words that can be formed from given letters

def words_from_letters_counter(words, letters):
    from collections import Counter
    letter_count = Counter(letters)
    result = []
    for word in words:
        word_count = Counter(word)
        if all(word_count[ch] <= letter_count.get(ch, 0) for ch in word):
            result.append(word)
    return result

def words_from_letters_manual(words, letters):
    letter_freq = {}
    for ch in letters:
        letter_freq[ch] = letter_freq.get(ch, 0) + 1
    result = []
    for word in words:
        word_freq = {}
        for ch in word:
            word_freq[ch] = word_freq.get(ch, 0) + 1
        valid = True
        for ch, count in word_freq.items():
            if count > letter_freq.get(ch, 0):
                valid = False
                break
        if valid:
            result.append(word)
    return result

# Example
words = ["cat", "bat", "rat", "tar", "art", "car"]
letters = "atr"
print(f"Words: {words}")
print(f"Letters: {letters}")
print("Using Counter:", words_from_letters_counter(words, letters))
print("Using manual dict:", words_from_letters_manual(words, letters))