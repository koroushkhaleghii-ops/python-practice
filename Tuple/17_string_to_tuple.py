# Exercise 17: Convert a string to a tuple of characters

def str_to_tuple_builtin():
    text = "Python"
    result = tuple(text)
    print("String:", text)
    print("Tuple of characters:", result)

def str_to_tuple_manual():
    text = "Python"
    result = ()
    for ch in text:
        result += (ch,)
    print("Manual conversion:", result)

# Example
str_to_tuple_builtin()
str_to_tuple_manual()