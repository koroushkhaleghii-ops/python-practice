# Exercise 15: Find the most frequent number in a list

def most_frequent(items):
    if not items:
        return None
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    
    max_count = -1
    most_common = None
    for key, value in freq.items():
        if value > max_count:
            max_count = value
            most_common = key
    return most_common

# Example
my_list = [1, 3, 2, 3, 4, 3, 5, 3]
print("Most frequent:", most_frequent(my_list))