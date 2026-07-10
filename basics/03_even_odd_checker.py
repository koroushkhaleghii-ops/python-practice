"""
Exercise 3: Even or Odd Checker
Take an integer and check if it is even or odd.
"""

def check_even_odd():
    number = int(input("Enter an integer: "))
    if number % 2 == 0:
        print(number, "is Even.")
    else:
        print(number, "is Odd.")

check_even_odd()