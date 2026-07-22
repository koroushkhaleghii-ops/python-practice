# Exercise 14: Create a dictionary from two lists (keys and values)

def create_dict(keys, values):
    if len(keys) != len(values):
        return None
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    return result

# example
keys = ["name", "age", "city"]
values = ["rahi", 34, "kashan"]
print("Keys:", keys)
print("Values:", values)
print("Using manual loop:", create_dict(keys, values))