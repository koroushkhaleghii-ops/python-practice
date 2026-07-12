# Exercise 19: Get 10 numbers and find the largest and smallest without using max()/min()

largest = None
smallest = None

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)