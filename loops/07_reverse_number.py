# Exercise 7: Reverse a number

num = int(input("Enter a number: "))
temp = abs(num)
reversed_num = 0
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10
if num < 0:
    reversed_num = -reversed_num  
print("Reversed number:", reversed_num)