# Exercise 17: Print the complete multiplication table from 1 to 10 using nested loops

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()  