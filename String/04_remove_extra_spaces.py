# Exercise 4: Remove extra spaces from a string

def clean_spaces(text):
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
print("result:", clean_spaces(text))