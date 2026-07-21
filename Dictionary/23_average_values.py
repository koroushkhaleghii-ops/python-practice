# Exercise 23: Find the average of all values in a dictionary

def avg_values_builtin(d):
    if not d:
        return None
    return sum(d.values()) / len(d)

def avg_values_manual(d):
    if not d:
        return None
    total = 0
    count = 0
    for value in d.values():
        total += value
        count += 1
    return total / count

# Example
scores = {"Kourosh": 22, "Asghar": 30, "Reza": 17, "Soheil": 19}
print(f"Dictionary: {scores}")
print("Using sum/len:", avg_values_builtin(scores))
print("Using manual loop:", avg_values_manual(scores))