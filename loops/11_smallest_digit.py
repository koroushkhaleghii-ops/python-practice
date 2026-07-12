# Exercise 11: Find the smallest digit of a number

num = int(input("Enter a number: "))
temp = abs(num)
min_digit = 9
if temp == 0:
    min_digit = 0
else:
    while temp > 0:
        digit = temp % 10
        if digit < min_digit:
            min_digit = digit
        temp //= 10
print("Smallest digit:", min_digit)