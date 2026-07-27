# Exercise 29 : Group anagrams from a list of words
# Example: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

def group_anagrams(words):
    def sort_word(word):
        chars = list(word)
        n = len(chars)
        for i in range(n):
            for j in range(i + 1, n):
                if chars[i] > chars[j]:
                    chars[i], chars[j] = chars[j], chars[i]
        return ''.join(chars)
    
    groups = {}
    for word in words:
        sorted_word = sort_word(word)
        if sorted_word in groups:
            groups[sorted_word].append(word)
        else:
            groups[sorted_word] = [word]
    return list(groups.values())

# Example
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(f"Words: {words}")
print("\nUsing manual sorting + dict:")
print(group_anagrams(words))