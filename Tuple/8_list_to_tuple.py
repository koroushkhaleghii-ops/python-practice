# Exercise 8: Convert a list to a tuple

def convert_builtin():
    my_list = [1, 2, 3, 4, 5]
    my_tuple = tuple(my_list)
    print("List:", my_list)
    print("Tuple:", my_tuple)
    print("Type of tuple:", type(my_tuple))

def convert_manual():
    my_list = [1, 2, 3, 4, 5]
    my_tuple = ()
    for item in my_list:
        my_tuple += (item,)
    print("Manual conversion:", my_tuple)

# Example
convert_builtin()
convert_manual()