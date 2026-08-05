# Exercise 15: Use tuple as dictionary key

def dict_with_tuple_key():
    coordinates = {
        (0, 0): "Origin",
        (1, 2): "Point A",
        (-1, 3): "Point B"
    }
    print("Dictionary:", coordinates)
    print("Value for (1,2):", coordinates[(1, 2)])

def dict_iterate_keys():
    coordinates = {
        (0, 0): "Origin",
        (1, 2): "Point A",
        (-1, 3): "Point B"
    }
    for key, value in coordinates.items():
        print(f"Key {key} -> {value}")

# Example
dict_with_tuple_key()
dict_iterate_keys()