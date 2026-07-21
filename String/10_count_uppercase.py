# Exercise 10: Count uppercase letters in a string

def count_upper(text):
    count = 0
    for ch in text:
        if ch.isupper():
            count += 1
    return count

# Example
sample = "World Cup 2026"
print(f"Text: {sample}")
print("Using manual loop:", count_upper(sample))