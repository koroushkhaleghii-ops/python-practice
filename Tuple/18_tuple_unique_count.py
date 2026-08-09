# Exercise 18: Count unique elements in a tuple

def unique_count_set():
    numbers = (1, 2, 2, 3, 3, 3, 4)
    unique_count = len(set(numbers))
    print("Tuple:", numbers)
    print("Unique count using set():", unique_count)

def unique_count_manual():
    numbers = (1, 2, 2, 3, 3, 3, 4)
    seen = []
    for num in numbers:
        if num not in seen:
            seen.append(num)
    print("Unique count manually:", len(seen))

# Example
unique_count_set()
unique_count_manual()