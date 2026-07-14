# Exercise 12: Function to return common elements between two lists

def find_common(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

# Example 
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
result = find_common(a, b)
print("Common elements:", result)