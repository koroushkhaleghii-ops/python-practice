# Exercise 21: Remove duplicates from a list without using set()
def remove_duplicates(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique

# Example
sample = [1, 2, 2, 3, 4, 4, 5]
print(f"Original: {sample}")
print("Result : ", remove_duplicates(sample))