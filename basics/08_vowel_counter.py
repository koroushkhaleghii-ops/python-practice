"""
Exercise 8: Vowel Counter
Count the number of vowels (a, e, i, o, u) in a string.
"""

def count_vowels():
    text = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count = count + 1
    print("The number of vowels is:", count)

count_vowels()