# Exercise 3: Check if a string is a palindrome

def is_palindrome_slicing(text):
    clean = text.lower().replace(" ", "")
    return clean == clean[::-1]


text = "kourosh"
print("Result:", is_palindrome_slicing(text))