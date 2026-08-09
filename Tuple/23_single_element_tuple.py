# Exercise 23: Create a tuple with one element (comma is important)

def single_tuple_with_comma():
    t1 = (5,)
    print("With comma:", t1)
    print("Type:", type(t1))
    print("Length:", len(t1))

def single_tuple_without_comma():
    t2 = (5)
    print("Without comma:", t2)
    print("Type:", type(t2))  

# Example
single_tuple_with_comma()
single_tuple_without_comma()