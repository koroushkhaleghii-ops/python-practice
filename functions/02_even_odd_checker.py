# Exercise 2: Function to check if a number is even or odd

def is_even(number):
    if number%2==0:
        print(number,"is even.")
    else:
        print(number,"is odd.")    
    
#example 
digit = int(input("enter your number: "))
is_even(digit)    