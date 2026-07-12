# Exercise 18: Get numbers from user until 0 is entered, then show sum and average

total = 0
count = 0

while True:
    num = int(input("Enter a number (enter 0 to stop): "))
    if num == 0:
        break
    total += num
    count += 1

if count == 0:
    print("No numbers were entered.")
else:
    avg = total / count
    print("Sum of numbers:", total)
    print("Average of numbers:", avg)