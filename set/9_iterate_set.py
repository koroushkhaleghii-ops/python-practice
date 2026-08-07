# Exercise 10: Iterate over a set

def iterate_simple():
    numbers = {10, 20, 30, 40, 50}
    print("Set:", numbers)
    print("Elements:")
    for num in numbers:
        print(num, end=" ")
    print()

def iterate_with_enumerate():
    numbers = {10, 20, 30, 40, 50}
    for index, value in enumerate(numbers):
        print(f"Index {index}: {value}")

# Example
iterate_simple()
iterate_with_enumerate()