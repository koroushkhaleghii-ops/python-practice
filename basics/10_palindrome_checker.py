"""
Exercise 10: Palindrome Checker
Check if a word reads the same backward (e.g., radar, madam).
"""

def check_palindrome():
    word = input("Enter a word: ")
    cleaned_word = word.lower()
    reversed_word = cleaned_word[::-1]
    
    if cleaned_word == reversed_word:
        print(word, "is a Palindrome.")
    else:
        print(word, "is NOT a Palindrome.")

check_palindrome()