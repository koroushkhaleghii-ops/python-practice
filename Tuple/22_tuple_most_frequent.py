# Exercise 22: Find the most frequent element in a tuple

from collections import Counter

def most_frequent_counter():
    numbers = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
    counter = Counter(numbers)
    most_common = counter.most_common(1)[0]
    print("Tuple:", numbers)
    print("Most frequent element:", most_common[0])
    print("Occurrences:", most_common[1])

def most_frequent_manual():
    numbers = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    max_count = -1
    most_frequent = None
    for key, value in freq.items():
        if value > max_count:
            max_count = value
            most_frequent = key
    print("Manual method - Most frequent:", most_frequent)
    print("Occurrences:", max_count)

# Example
most_frequent_counter()
most_frequent_manual()