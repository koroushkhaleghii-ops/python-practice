# Exercise 10: Concatenate two tuples

def concat_builtin():
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    result = tuple1 + tuple2
    print("Tuple 1:", tuple1)
    print("Tuple 2:", tuple2)
    print("Concatenated (+):", result)

def concat_manual():
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    result = ()
    for item in tuple1:
        result += (item,)
    for item in tuple2:
        result += (item,)
    print("Manual concatenation:", result)

# Example
concat_builtin()
concat_manual()