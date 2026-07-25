# Exercise 23: Check if a list is sorted (ascending, descending, or unsorted)

def check_sorted_builtin(numbers):
    if numbers == sorted(numbers):
        return "Ascending"
    elif numbers == sorted(numbers, reverse=True):
        return "Descending"
    else:
        return "Unsorted"

def check_sorted_manual(numbers):
    if len(numbers) < 2:
        return 
    ascending = True
    descending = True
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            ascending = False
        if numbers[i] < numbers[i + 1]:
            descending = False
    if ascending:
        return "Ascending"
    elif descending:
        return "Descending"
    else:
        return "Unsorted"

# Example
sample = [1, 2, 3, 4, 5]
print(f"List: {sample}")
print("Using built-in:", check_sorted_builtin(sample))
print("Using manual:", check_sorted_manual(sample))