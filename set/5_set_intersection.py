# Exercise 5: Intersection of two sets

def intersection_operator():
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    result = a & b
    print("A:", a)
    print("B:", b)
    print("Intersection (&):", result)

def intersection_method():
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    result = a.intersection(b)
    print("Intersection using intersection():", result)

# Example
intersection_operator()
intersection_method()