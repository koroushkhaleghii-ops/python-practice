# Exercise 11: Function to remove duplicates from a list (without using set)

def remove_duplicates(items):
    unique = []
    for item in items:
        if item not in unique:  
            unique.append(item)
    return unique

# Example 
my_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
result = remove_duplicates(my_list)
print("List after removing duplicates:", result)