# Exercise 7: Function to count vowels in a string

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Example 
user_text = input("Enter a string: ")
vowel_count = count_vowels(user_text)
print("Number of vowels:", vowel_count)