# Exercise 20: Check if a string can become palindrome by deleting at most one char

def valid_palindrome(s):
    def is_palindrome(chars):
        return chars == chars[::-1]
    
    chars = list(s)
    if is_palindrome(chars):
        return True
    
    for i in range(len(chars)):
        temp = chars[:i] + chars[i+1:]
        if is_palindrome(temp):
            return True
    return False

# Example
test1 = "aba"
test2 = "abca"
test3 = "abc"
print(f"'{test1}' -> {valid_palindrome(test1)}")
print(f"'{test2}' -> {valid_palindrome(test2)}")
print(f"'{test3}' -> {valid_palindrome(test3)}")