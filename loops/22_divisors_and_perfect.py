# Exercise 5: Find all divisors of a number and check if it is a Perfect Number

num = int(input("enter a number: "))
divisors = []

for i in range(1, num + 1):
    if num % i == 0:
        divisors.append(i)

print("Divisors of", num, "are:", divisors)

sum_of_proper_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_of_proper_divisors += i

if sum_of_proper_divisors == num:
    print(num, "is a Perfect Number!")
else:
    print(num, "is not a Perfect Number.")