# Exercise 9: Function to count words in a string

def count_words(text):
    if text.strip() == "":  
        return 0
    words = text.split() 
    return len(words)

# Example 
user_text = input("Enter a string: ")
print("Number of words:", count_words(user_text))