# Exercise 6: Count odd numbers in a list

def count_odd(numbers):
    count = 0
    for num in numbers:
        if num % 2 != 0:
            count += 1
    return count

# Example
my_list = [1, 2, 3, 4, 5, 6]
print("Odd count:", count_odd(my_list))