# Exercise 15: Count frequency of letters in a word

word = "python programming"

word = word.replace(" ", "")

frequency = {}
for letter in word:
    frequency[letter] = frequency.get(letter, 0) + 1

print("Letter frequency:")
for letter, count in frequency.items():
    print(f"{letter}: {count}")