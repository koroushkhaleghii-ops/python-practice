# Exercise 16: Create an empty tuple and check if it's empty

def empty_check_builtin():
    empty = ()
    print("Tuple:", empty)
    print("Is empty using len():", len(empty) == 0)

def empty_check_truthy():
    empty = (1,2)
    print("Is empty using truthiness:", not empty)

# Example
empty_check_builtin()
empty_check_truthy()