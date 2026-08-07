# Exercise 8: Check subset and superset

def subset_superset():
    a = {1, 2}
    b = {1, 2, 3, 4}
    print("A:", a)
    print("B:", b)
    print("A is subset of B:", a.issubset(b))
    print("B is superset of A:", b.issuperset(a))

def subset_manual():
    a = {1, 2}
    b = {1, 2, 3, 4}
    is_subset = True
    for item in a:
        if item not in b:
            is_subset = False
            break
    print("A subset of B (manual):", is_subset)

# Example
subset_superset()
subset_manual()