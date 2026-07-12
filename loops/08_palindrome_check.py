# Exercise 8: Check if a number is palindrome

num = int(input("Enter a number: "))
original = num
temp = abs(original)
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
if original < 0:
    rev = -rev
if original == rev:
    print(original, "is a palindrome")
else:
    print(original, "is not a palindrome")