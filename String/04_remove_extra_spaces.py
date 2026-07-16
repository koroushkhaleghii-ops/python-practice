# Exercise 4: Remove extra spaces from a string

def clean_spaces_manual(text):
    """روش دستی با حلقه (آموزشی)"""
    result = ""
    in_space = False
    for ch in text:
        if ch == ' ':
            if not in_space:
                result += ch
                in_space = True
        else:
            result += ch
            in_space = False
    return result.strip()  


text = "  hello  kourosh  how   are   you?  "
print(f"Original: '{text}'")
print("Using manual loop:", clean_spaces_manual(text))