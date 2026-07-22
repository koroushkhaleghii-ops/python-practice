# Exercise 18: Convert dictionary to list of (key, value) tuples

def dict_to_list_builtin(d):
    return list(d.items())

def dict_to_list_manual(d):
    result = []
    for key, value in d.items():
        result.append((key, value))
    return result

# Example
sample_dict = {"a": 1, "b": 2, "c": 3}
print(f"Dictionary: {sample_dict}")
print("Using list(items):", dict_to_list_builtin(sample_dict))
print("Using manual loop:", dict_to_list_manual(sample_dict))