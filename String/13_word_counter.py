#Exercise 13 : Write a Python program that counts the frequency of each word in a given input string.

from collections import Counter

input_text = "I love python because IDK"
words = input_text.split()
result = Counter(words)

for word, count in result.items():
    print(f"{word} : {count}")