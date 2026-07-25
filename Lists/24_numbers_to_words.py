# Exercise 24: Convert numbers to their word equivalents

def numbers_to_words(numbers):
    words = []
    for num in numbers:
        if num == 1:
            words.append("one")
        elif num == 2:
            words.append("two")
        elif num == 3:
            words.append("three")
        elif num == 4:
            words.append("four")
        elif num == 5:
            words.append("five")
        elif num == 6:
            words.append("six")
        elif num == 7:
            words.append("seven")
        elif num == 8:
            words.append("eight")
        elif num == 9:
            words.append("nine")
        else:
            words.append(str(num))
    return words

# Example
sample = [1, 3, 5, 7, 9]
print(f"Numbers: {sample}")
print("Result:", numbers_to_words(sample))