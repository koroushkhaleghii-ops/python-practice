# Exercise 3: Find LCM of two numbers

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

x = abs(number1)
y = abs(number2)
while y != 0:
    remainder = x % y
    x = y
    y = remainder
gcd = x

lcm = abs(number1 * number2) // gcd
print("LCM of", number1, "and", number2, "is:", lcm)