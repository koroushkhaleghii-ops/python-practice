"""
Exercise 5: Sum of Numbers from 1 to N
Calculate the sum of all numbers from 1 to N using a loop.
"""

def sum_1_to_n():
    n = int(input("Enter a positive integer N: "))
    total = 0
    for i in range(1, n + 1):
        total = total + i
    print("The sum of numbers from 1 to", n, "is:", total)

sum_1_to_n()