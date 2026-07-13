# Exercise 3: Function to find the largest among three numbers

def find_largest(a , b , c):
    if a >= b and a >= c:
        return print("the largest number is: ",a)
    elif b >= a and b >= c :
        return  print("the largest number is: ",b)
    else :
        print("the largest number is: ",c)

num1 = int(input("ernter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))

find_largest(num1 , num2 , num3)