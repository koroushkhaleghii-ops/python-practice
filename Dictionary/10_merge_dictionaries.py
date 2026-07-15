# Exercise 10: Merge two dictionaries

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5, "b": 10}  

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)


merged1 = dict1.copy()  
merged1.update(dict2)
print("Merged using update():", merged1)
