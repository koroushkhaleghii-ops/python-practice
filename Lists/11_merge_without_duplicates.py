# Exercise 11: Merge two lists without duplicates

def merge_lists(list1, list2):
    merged = list1.copy()  
    for item in list2:
        if item not in merged:
            merged.append(item)
    return merged

# Example
a = [1, 2, 3]
b = [3, 4, 5]
print("Merged:", merge_lists(a, b))