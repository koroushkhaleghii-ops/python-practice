# Exercise 2: Print even numbers from 1 to 100
#1:
for num in range(1,101):
    if num%2==0:
        print(num)

print("\nanother way :\n")        
#2:
for num in range(2, 101, 2):
    print(num)