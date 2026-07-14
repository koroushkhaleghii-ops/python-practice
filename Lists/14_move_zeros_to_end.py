# Exercise 14: Move all zeros to the end of the list

def move_zeros(numbers):
    non_zero = []
    zeros = []
    for num in numbers:
        if num == 0:
            zeros.append(num)
        else:
            non_zero.append(num)
    return non_zero + zeros  

# Example
my_list = [0, 1, 0, 3, 12, 0]
print("After moving zeros:", move_zeros(my_list))