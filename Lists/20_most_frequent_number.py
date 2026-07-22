# Exercise 20: Find the most frequent number in a list

from collections import Counter

def most_frequent_counter(numbers):
    if not numbers:
        return None
    counter = Counter(numbers)
    return counter.most_common(1)[0]  

# Example
sample = [1, 2, 2, 3, 3, 3, 4]
print(f"List: {sample}")
print("Using Counter:", most_frequent_counter(sample))
