# Exercise 17: Remove all negative numbers from a list

def remove_negatives_comprehension(numbers):
    return [num for num in numbers if num >= 0]

def remove_negatives_manual(numbers):
    result = []
    for num in numbers:
        if num >= 0:
            result.append(num)
    return result

# Example
sample = [1, -2, 3, -4, 5, -6, 0]
print(f"Original: {sample}")
print("Using comprehension:", remove_negatives_comprehension(sample))
print("Using manual loop:", remove_negatives_manual(sample))