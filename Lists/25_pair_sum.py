# Exercise 25: Find pairs that sum to a target value

def find_pairs(numbers, target):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))
    return pairs


# Example
numbers = [2, 4, 3, 6, 1, 5]
target = 7
print(f"Numbers: {numbers}, Target: {target}")
print("Result:", find_pairs(numbers, target))
