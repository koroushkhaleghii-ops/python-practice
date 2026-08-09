# Exercise 21: Check if a tuple is sorted in ascending order

def is_sorted_builtin():
    t1 = (1, 2, 3, 4, 5)
    t2 = (1, 3, 2, 4, 5)
    print("Tuple 1:", t1)
    print("Is sorted:", t1 == tuple(sorted(t1)))
    print("Tuple 2:", t2)
    print("Is sorted:", t2 == tuple(sorted(t2)))

def is_sorted_manual():
    t1 = (1, 2, 3, 4, 5)
    is_sorted = True
    for i in range(len(t1) - 1):
        if t1[i] > t1[i + 1]:
            is_sorted = False
            break
    print("Manual check for t1:", is_sorted)

# Example
is_sorted_builtin()
is_sorted_manual()