# Exercise 7: Find the largest number without max()

def max_manual():
    numbers = (15, 42, 7, 28, 33)
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    print("Tuple:", numbers)
    print("Largest using manual loop:", max_num)

def max_builtin():
    numbers = (15, 42, 7, 28, 33)
    print("Largest using max():", max(numbers))

# Example
max_manual()
max_builtin()