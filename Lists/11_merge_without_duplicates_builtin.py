# Exercise 11: Merge two lists without duplicates using set union

a = [1, 2, 3]
b = [3, 4, 5]
merged = list(set(a) | set(b)) 
print("Merged without duplicates:", merged)