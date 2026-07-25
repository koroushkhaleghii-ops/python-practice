# Exercise 18: Check if a string is a substring of another (without using 'in')

def is_substring(text, sub):
    if len(sub) > len(text):
        return False
    for i in range(len(text) - len(sub) + 1):
        match = True
        for j in range(len(sub)):
            if text[i + j] != sub[j]:
                match = False
                break
        if match:
            return True
    return False

# Example
text = "Hi kourosh"
sub = "Hi"
print(f"Text: '{text}', Substring: '{sub}'")
print("Result:", is_substring(text, sub))