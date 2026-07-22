# Exercise 19: Count frequency of each number in a list

from collections import Counter

def frequency_counter(numbers):
    return dict(Counter(numbers))

def frequency_manual(numbers):
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    return freq

# Example
sample = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(f"List: {sample}")
print("Using Counter:", frequency_counter(sample))
print("Using manual dict:", frequency_manual(sample))