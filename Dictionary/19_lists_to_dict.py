# Exercise 22: Create a dictionary from two lists (keys and values)

def dict_from_zip(keys, values):
    if len(keys) != len(values):
        return None
    return dict(zip(keys, values))

def dict_from_manual(keys, values):
    if len(keys) != len(values):
        return None
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    return result

# Example
keys = ["name", "age", "city"]
values = ["Kourosh", 22, "Ardebil"]
print(f"Keys: {keys}")
print(f"Values: {values}")
print("Using zip:", dict_from_zip(keys, values))
print("Using manual loop:", dict_from_manual(keys, values))