# Exercise 24: Find the key with the maximum value

def max_key(d):
    if not d:
        return None
    max_key = None
    max_value = float('-inf')
    for key, value in d.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key

# Example
scores = {"Kourosh": 18, "Kaveh": 20, "Dar": 15, "Zal": 19}
print(f"Dictionary: {scores}")
print("Using manual loop:", max_key(scores))