# Exercise 4: Union of two sets

def union_operator():
    a = {1, 2, 3}
    b = {3, 4, 5}
    result = a | b
    print("A:", a)
    print("B:", b)
    print("Union (|):", result)

def union_method():
    a = {1, 2, 3}
    b = {3, 4, 5}
    result = a.union(b)
    print("Union using union():", result)

# Example
union_operator()
union_method()