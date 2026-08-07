# Exercise 2: Remove elements from a set

def remove_demo():
    my_set = {1, 2, 3, 4}
    print("Original:", my_set)
    my_set.remove(2)     
    print("After remove(2):", my_set)
    my_set.discard(5)     
    print("After discard(5):", my_set)

def remove_with_check():
    my_set = {1, 2, 3}
    item = 4
    if item in my_set:
        my_set.remove(item)
        print(f"Removed {item}")
    else:
        print(f"{item} not in set")

# Example
remove_demo()
remove_with_check()