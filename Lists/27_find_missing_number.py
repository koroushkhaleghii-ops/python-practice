# Exercise 9: Find missing number in a consecutive sequence

def find_missing_loop(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] + 1 != numbers[i + 1]:
            return numbers[i] + 1
    return None

# Example
sequence = [1, 2, 3, 4, 6, 7, 8]
print(f"Sequence: {sequence}")
print("The missig number is equal to:", find_missing_loop(sequence))