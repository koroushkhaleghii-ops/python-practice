# Exercise 10: Function to return only even numbers from a list

def get_even_numbers(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

# Example 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = get_even_numbers(my_list)
print("Even numbers:", result)