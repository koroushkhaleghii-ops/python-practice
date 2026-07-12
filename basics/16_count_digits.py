# Goal:Count digits of a number

number = int(input("enter a number: "))
digit_count = len(str(abs(number)))
print("Number of digits:",digit_count)