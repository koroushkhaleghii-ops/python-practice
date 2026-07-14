# Exercise 9: Find second largest using sorted() and set()

my_list = [10, 5, 20, 8, 15]
sorted_unique = sorted(set(my_list))  
if len(sorted_unique) >= 2:
    print("Second largest:", sorted_unique[-2])
else:
    print("Not enough unique elements")