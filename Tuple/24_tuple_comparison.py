# Exercise 24: Compare two tuples lexicographically

def compare_simple():
    t1 = (1, 2, 3)
    t2 = (1, 2, 4)
    t3 = (1, 2, 3)
    print("t1:", t1)
    print("t2:", t2)
    print("t3:", t3)
    print("t1 < t2:", t1 < t2)
    print("t1 == t3:", t1 == t3)
    print("t2 > t1:", t2 > t1)

def compare_different_lengths():
    t1 = (1, 2)
    t2 = (1, 2, 3)
    print("t1:", t1)
    print("t2:", t2)
    print("t1 < t2:", t1 < t2)  


# Example
compare_simple()
compare_different_lengths()