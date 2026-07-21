# Exercise 18: Count lowercase letters in a string
def count_lower(text):
    count = 0
    for ch in text:
        if ch.islower():
            count += 1
    return count

# Example
sample = "The 2026 World Cup final was between Argentina and Spain."
print(f"Text: {sample}")
print("Using manual loop:", count_lower(sample))