"""
Exercise 9: Find Min and Max in a List
Take 5 numbers, store them in a list, and find min and max.
"""

def find_min_max():
    numbers = []
    
    for i in range(5):
        num = float(input("Enter number " + str(i+1) + ": "))
        numbers.append(num)
    
    minimum = min(numbers)
    maximum = max(numbers)
    
    print("Numbers:", numbers)
    print("Minimum:", minimum)
    print("Maximum:", maximum)

find_min_max()