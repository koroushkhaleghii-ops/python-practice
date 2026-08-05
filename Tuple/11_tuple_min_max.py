# Exercise 11: Find min and max of a tuple

def min_max_builtin():
    numbers = (11, 56, 7, 25, 33)
    print("Tuple:", numbers)
    print("Min using min():", min(numbers))
    print("Max using max():", max(numbers))

def min_max_manual():
    numbers = (11, 56, 7, 25, 33)
    min_val = numbers[0]
    max_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    print("Min manually:", min_val)
    print("Max manually:", max_val)

# Example
min_max_builtin()
min_max_manual()