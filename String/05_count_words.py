# Exercise 5: Count words in a text

def count_words_split(text):
    return len(text.split())


text = "football"
print(f"Text: {text}")
print("Using split:", count_words_split(text))
