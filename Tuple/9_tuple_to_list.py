# Exercise 9: Convert a tuple to a list

def convert_builtin():
    my_tuple = (1, 2, 3, 4, 5)
    my_list = list(my_tuple)
    print("Tuple:", my_tuple)
    print("List:", my_list)
    print("Type of list:", type(my_list))

def convert_manual():
    my_tuple = (1, 2, 3, 4, 5)
    my_list = []
    for item in my_tuple:
        my_list.append(item)
    print("Manual conversion:", my_list)

# Example
convert_builtin()
convert_manual()