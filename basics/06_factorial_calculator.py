"""
Exercise 6: Factorial Calculator
Calculate the factorial of a non-negative integer.
"""

def calculate_factorial():
    n = int(input("Enter a non-negative integer: "))
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    print("The factorial of", n, "is:", factorial)

calculate_factorial()