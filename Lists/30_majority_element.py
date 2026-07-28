# Exercise 30: Find the majority element (appears more than n/2 times)

from collections import Counter

def majority_counter(arr):
    n = len(arr)
    counter = Counter(arr)
    for num, count in counter.items():
        if count > n // 2:
            return num
    return None

def majority_boyer_moore(arr):
    candidate = None
    count = 0
    
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    if candidate is not None:
        if arr.count(candidate) > len(arr) // 2:
            return candidate
    return None

# Example
sample1 = [3, 2, 3]
sample2 = [2, 2, 1, 1, 1, 2, 2]
print(f"Sample 1: {sample1} -> {majority_counter(sample1)}")
print(f"Sample 2: {sample2} -> {majority_boyer_moore(sample2)}")