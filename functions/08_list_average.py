# Exercise 8: Function to calculate the average of numbers in a list

def calculate_average(numbers):
    if len(numbers) == 0:
        return None   
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

# Example 
user_list = []
n = int(input("How many numbers do you want to enter? "))
for i in range(n):
    value = float(input(f"Enter number {i+1}: "))
    user_list.append(value)

avg = calculate_average(user_list)
if avg is None:
    print("The list is empty, cannot calculate average.")
else:
    print("Average of the list is:", avg)