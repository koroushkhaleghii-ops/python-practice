# Exercise 3: Merge two dictionaries, summing values for common keys

from collections import Counter

def merge_sum_manual(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

def merge_sum_counter(dict1, dict2):
    return dict(Counter(dict1) + Counter(dict2))

# Example
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(f"Dict A: {d1}")
print(f"Dict B: {d2}")
print("Using manual loop:", merge_sum_manual(d1, d2))
print("Using Counter:", merge_sum_counter(d1, d2))