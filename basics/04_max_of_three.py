"""
Exercise 4: Maximum of Three Numbers
Find the largest number among three inputs.
"""

def find_max_of_three():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    
    if a >= b and a >= c:
        maximum = a
    elif b >= a and b >= c:
        maximum = b
    else:
        maximum = c
    
    print("The maximum number is:", maximum)

find_max_of_three()