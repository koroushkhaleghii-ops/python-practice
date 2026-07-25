# Exercise 28: Find the first number that appears exactly once

from collections import Counter

def first_unique_counter(numbers):
    freq = Counter(numbers)
    for num in numbers:
        if freq[num] == 1:
            return num
    return None

def first_unique_manual(numbers):
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    for num in numbers:
        if freq[num] == 1:
            return num
    return None

# Example
sample = [4, 5, 1, 2, 5, 4, 3]
print(f"List: {sample}")
print("Using Counter:", first_unique_counter(sample))
print("Using manual dict:", first_unique_manual(sample))