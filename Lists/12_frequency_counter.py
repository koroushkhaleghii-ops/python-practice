# Exercise 12: Count frequency of each element in a list

def count_frequency(items):
    freq = {}
    for item in items:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

# Example
my_list = [1, 2, 2, 3, 3, 3, 4]
print("Frequency:", count_frequency(my_list))