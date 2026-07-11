"""
Goal: Take an English sentence or paragraph.
1. Split all the words (handle spaces and punctuation).
2. Build a dictionary where the key is the word and the value is the count.
3. Finally, print the top 3 most frequent words.

"""

text = "apple banana apple orange grape banana apple apple"

# Basic cleaning (removing dots and commas)
cleaned_text = text.replace(".", "").replace(",", "")
words = cleaned_text.split()

freq = {}
for word in words:
    # This line is golden! If the key doesn't exist, it returns 0 and adds 1
    freq[word] = freq.get(word, 0) + 1  

print(f"Frequency dictionary: {freq}")

# Finding top 3 frequent words using sort
sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print(f"Top 3 most frequent words: {sorted_words[:3]}")