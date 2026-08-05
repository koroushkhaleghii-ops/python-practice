# Exercise 13: Check if an element exists in a tuple

def contains_in():
    fruits = ("apple", "banana", "cherry")
    search = "banana"
    print("Tuple:", fruits)
    print(f"'{search}' in tuple:", search in fruits)

def contains_manual():
    fruits = ("apple", "banana", "cherry")
    search = "banana"
    found = False
    for item in fruits:
        if item == search:
            found = True
            break
    print(f"'{search}' found manually:", found)

# Example
contains_in()
contains_manual()