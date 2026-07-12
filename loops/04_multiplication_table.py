# Exercise 4: Print multiplication table of a given number

number = int(input("enter your number: "))
for digit in range(1,11):
    print(f"{number} X {digit} =",digit*number)