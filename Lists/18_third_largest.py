# Exercise 18: Find the third largest number in a list

def third_largest_sort(numbers):
    if len(numbers) < 3:
        return None
    unique_sorted = sorted(set(numbers), reverse=True)
    if len(unique_sorted) < 3:
        return None
    return unique_sorted[2]

def third_largest_traverse(numbers):
    if len(numbers) < 3:
        return None
    first = second = third = float('-inf')
    for num in numbers:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second and num != first:
            third = second
            second = num
        elif num > third and num != second and num != first:
            third = num
    return third if third != float('-inf') else None

# Example
sample = [10, 5, 20, 8, 15, 20]
print(f"List: {sample}")
print("Using sort/set:", third_largest_sort(sample))
print("Using single traverse:", third_largest_traverse(sample))