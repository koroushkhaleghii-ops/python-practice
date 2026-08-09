# Exercise 19: Slicing a tuple

def slicing_basic():
    numbers = (10, 20, 30, 40, 50, 60)
    print("Original:", numbers)
    print("First 3 elements:", numbers[:3])
    print("Last 2 elements:", numbers[-2:])
    print("Elements 1 to 4:", numbers[1:4])
    print("Every second element:", numbers[::2])

def slicing_with_step():
    numbers = (10, 20, 30, 40, 50, 60)
    print("Reversed tuple:", numbers[::-1])

# Example
slicing_basic()
slicing_with_step()