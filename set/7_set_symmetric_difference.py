# Exercise 7: Symmetric difference of two sets

def sym_diff_operator():
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    result = a ^ b
    print("A:", a)
    print("B:", b)
    print("Symmetric diff (^):", result)

def sym_diff_method():
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    result = a.symmetric_difference(b)
    print("Using symmetric_difference():", result)

# Example
sym_diff_operator()
sym_diff_method()