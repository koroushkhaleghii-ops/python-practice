# Exercise 5: Count even numbers in a list

def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

# Example
my_list = [1, 2, 3, 4, 5, 6]
print("Even count:", count_even(my_list))