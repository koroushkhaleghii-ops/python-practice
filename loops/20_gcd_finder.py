# Exercise 2: Find GCD of two numbers using only loops (Euclidean algorithm)

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

x = abs(number1)
y = abs(number2)

while y != 0:
    remainder = x % y
    x = y
    y = remainder

gcd = x
print("GCD of", number1, "and", number2, "is:", gcd)