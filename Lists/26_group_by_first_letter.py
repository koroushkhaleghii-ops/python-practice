# Exercise 7: Group words by their first letter

def group_by_first_letter(words):
    groups = {}
    for word in words:
        first = word[0].lower()
        if first in groups:
            groups[first].append(word)
        else:
            groups[first] = [word]
    return groups

# Example
words = ["apple", "banana", "cherry", "apricot", "blueberry", "grape"]
print(f"Words: {words}")
print("Result:", group_by_first_letter(words))