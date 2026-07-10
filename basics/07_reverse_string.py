"""
Exercise 7: Reverse a String
Reverse the input string using slicing.
"""

def reverse_string():
    text = input("Enter a string: ")
    reversed_text = text[::-1]
    print("Reversed string:", reversed_text)

reverse_string()