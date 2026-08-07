# Exercise 6: Difference of two sets

def difference_operator():
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    result = a - b
    print("A:", a)
    print("B:", b)
    print("A - B:", result)

def difference_method():
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    result = a.difference(b)
    print("A.difference(B):", result)

# Example
difference_operator()
difference_method()