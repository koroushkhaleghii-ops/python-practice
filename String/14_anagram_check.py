# Exercise 14: Check if two strings are anagrams

def are_anagrams_sort(str1, str2):
    return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())

def are_anagrams_count(str1, str2):
    s1 = str1.replace(" ", "").lower()
    s2 = str2.replace(" ", "").lower()
    if len(s1) != len(s2):
        return False
    freq = {}
    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s2:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1
    return True

# Example
s1 = "listen"
s2 = "silent"
print(f"'{s1}' and '{s2}'")
print("Using sorted:", are_anagrams_sort(s1, s2))
print("Using count dict:", are_anagrams_count(s1, s2))