# Exercise 31: Sort a list without using sort() - Bubble Sort

def bubble_sort_optimized(arr):
    result = arr.copy()
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result

def bubble_sort_basic(arr):
    result = arr.copy()
    n = len(result)
    for i in range(n):
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

# Example
sample = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {sample}")
print("Bubble sort (basic):", bubble_sort_basic(sample))
print("Bubble sort (optimized):", bubble_sort_optimized(sample))