# Exercise 6: Find the longest word
# way1:
def longest_word_max(text):

    words = text.split()
    if not words:
        return None
    return max(words, key=len)
# way2:
def longest_word_manual(text):
    words = text.split()
    if not words:
        return None
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

#example
text = "Python , kourosh , so much fun"
print(f"Text: {text}")
print("way1:", longest_word_max(text))
print("way2:", longest_word_manual(text))