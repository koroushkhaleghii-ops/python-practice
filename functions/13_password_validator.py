# Exercise 6: Function to validate a password
# Conditions: at least 8 characters, at least one digit, at least one uppercase letter

def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    
    has_digit = False
    has_upper = False
    
    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
    
    if not has_digit:
        return False, "Password must contain at least one digit."
    if not has_upper:
        return False, "Password must contain at least one uppercase letter."
    
    return True, "Password is valid."

# Example 
pwd = input("Enter a password: ")
is_valid, message = validate_password(pwd)
print(message)