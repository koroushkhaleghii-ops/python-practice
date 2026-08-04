# Exercise 3: Find the length of a tuple

def length_builtin():
    numbers = (10, 20, 30, 40, 50)
    print("Tuple:", numbers)
    print("Length using len():", len(numbers))

def length_manual():
    numbers = (10, 20, 30, 40, 50)
    count = 0
    for _ in numbers:
        count += 1
    print("Length using manual loop:", count)

# Example
length_builtin()
length_manual()