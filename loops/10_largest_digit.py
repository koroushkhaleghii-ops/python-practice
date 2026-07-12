# Exercise 10: Find the largest digit of a number

num = int(input("Enter a number: "))
temp = abs(num)
max_digit = 0
if temp == 0:
    max_digit = 0
else:
    while temp > 0:
        digit = temp % 10
        if digit > max_digit:
            max_digit = digit
        temp //= 10
print("Largest digit:", max_digit)