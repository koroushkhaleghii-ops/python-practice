# Exercise 32: Merge two sorted lists into one sorted list

def merge_sorted_two_pointers(list1, list2):
    i, j = 0, 0
    result = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result

def merge_sorted_builtin(list1, list2):
    return sorted(list1 + list2)

# Example
a = [1, 3, 5]
b = [2, 4, 6]
print(f"List A: {a}")
print(f"List B: {b}")
print("Using two pointers:", merge_sorted_two_pointers(a, b))
print("Using sorted():", merge_sorted_builtin(a, b))