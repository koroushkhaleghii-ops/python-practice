# Exercise 1: Check if a number is an Armstrong number

num = int(input("Enter a number: "))
original = num
temp = abs(num)
digit_count = len(str(temp)) 

sum_of_powers = 0
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** digit_count
    temp //= 10

if original == sum_of_powers:
    print(original, "is an Armstrong number")
else:
    print(original, "is not an Armstrong number")