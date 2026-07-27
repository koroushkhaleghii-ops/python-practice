# Exercise 19: Find the longest substring without repeating characters

def longest_unique_sliding_window(text):
    if not text:
        return ""
    left = 0
    max_length = 0
    start_index = 0
    seen = set()
    
    for right in range(len(text)):
        while text[right] in seen:
            seen.remove(text[left])
            left += 1
        seen.add(text[right])
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
            start_index = left
    return text[start_index:start_index + max_length]

def longest_unique_manual(text):
    if not text:
        return ""
    n = len(text)
    max_length = 0
    result = ""
    
    for i in range(n):
        seen = []
        for j in range(i, n):
            if text[j] in seen:
                break
            seen.append(text[j])
            current_length = j - i + 1
            if current_length > max_length:
                max_length = current_length
                result = text[i:j + 1]
    return result

# Example
sample = "abcabcbb"
print(f"Text: {sample}")
print("Using sliding window + set:", longest_unique_sliding_window(sample))
print("Using manual nested loops:", longest_unique_manual(sample))