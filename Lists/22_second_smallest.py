# Exercise 22: Find the second smallest number in a list

def second_smallest_sort(numbers):
    if len(numbers) < 2:
        return None
    unique_sorted = sorted(set(numbers))
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]

def second_smallest_traverse(numbers):
    if len(numbers) < 2:
        return None
    first = float('inf')
    second = float('inf')
    for num in numbers:
        if num < first:
            second = first
            first = num
        elif num < second and num != first:
            second = num
    return second if second != float('inf') else None

# Example
sample = [5, 2, 8, 1, 9, 3]
print(f"List: {sample}")
print("Using sort/set:", second_smallest_sort(sample))
print("Using single traverse:", second_smallest_traverse(sample))