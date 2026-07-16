# Exercise 1: Count alphabetic characters in a string

def count_letters_manual(text):
    count = 0
    for ch in text:
        if ch.isalpha():
            count += 1
    return count


text = "Kourosh , 22"
print(f"Text: {text}")
print("Using manual loop:", count_letters_manual(text))
