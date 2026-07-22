# Exercise 16: Count frequency of words in a sentence

sentence = "Python is great and Python is fun"

words = sentence.split() 

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequency:")
for word, count in frequency.items():
    print(f"{word}: {count}")