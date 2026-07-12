# Exercise 9: Sum of digits of a number

num = int(input("Enter a number: "))
temp = abs(num)
digit_sum = 0
while temp > 0:
    digit_sum += temp % 10
    temp //= 10
print("Sum of digits:", digit_sum)