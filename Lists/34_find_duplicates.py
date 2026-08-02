# Exercise 34: Find all duplicate numbers in a list

from collections import Counter


def find_duplicates_manual(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    result = []
    for num, count in freq.items():
        if count > 1:
            result.append(num)
    return result

def find_duplicates_set(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

# Example
sample = [4, 3, 2, 7, 8, 2, 3, 1]
print(f"Array: {sample}")
print("Using manual dict:", find_duplicates_manual(sample))
print("Using set:", find_duplicates_set(sample))