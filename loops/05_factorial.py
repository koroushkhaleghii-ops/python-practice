# Exercise 5: Calculate factorial of n

number = int(input("enter a number: "))
fact = 1
for digit in range(1 , number+1):
    fact *= digit
print("factorial of",number," is :",fact)    
     