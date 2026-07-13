# Exercise 6: Function to reverse a string

def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text 
    return reversed_text

# Example 
user_input = input("Enter a string: ")
reversed_input = reverse_string(user_input)
print("Reversed string:", reversed_input)