# Exercise 4: Count occurrences of a value in a tuple

def count_builtin():
    numbers = (1, 2, 3, 2, 4, 2, 5)
    print("Tuple:", numbers)
    print("Number of 2s using count():", numbers.count(2))

def count_manual():
    numbers = (1, 2, 3, 2, 4, 2, 5)
    target = 2
    count = 0
    for num in numbers:
        if num == target:
            count += 1
    print(f"Number of {target}s using manual loop:", count)

# Example
count_builtin()
count_manual()