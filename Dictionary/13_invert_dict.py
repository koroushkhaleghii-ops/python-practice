# Exercise 13: Invert key-value pairs (if values are unique)

def invert(original):
    values = list(original.values())
    if len(set(values)) != len(values):
        return None
    inverted = {}
    for key, value in original.items():
        inverted[value] = key
    return inverted

#example
original = {"digit1": 1, "digit2": 2, "digit3": 3}
print("Original:", original)
print("Inverted:", invert(original))
