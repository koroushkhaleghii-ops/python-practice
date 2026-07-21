# Exercise 12: Remove extra spaces (leading, trailing, multiple)


def clean_spaces(text):
    result = []
    in_space = False
    for ch in text:
        if ch == ' ':
            if not in_space:
                result.append(ch)
                in_space = True
        else:
            result.append(ch)
            in_space = False
    clean = ''.join(result).strip()
    return clean

# Example
sample = "  Hello   MY friend  How   are   you?  "
print(f"Original: '{sample}'")
print("Using manual loop:", clean_spaces(sample))