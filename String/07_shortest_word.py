# Exercise 7: Find the shortest word

# way3:
def shortest_word_min(text):
    words = text.split()
    if not words:
        return None
    return min(words, key=len)
# way2:
def shortest_word_manual(text):
    words = text.split()
    if not words:
        return None
    shortest = words[0]
    for word in words:
        if len(word) < len(shortest):
            shortest = word
    return shortest

#example
text = "Python it's cool"
print(f"Text: {text}")
print("way1 :", shortest_word_min(text))
print("way2 :", shortest_word_manual(text))