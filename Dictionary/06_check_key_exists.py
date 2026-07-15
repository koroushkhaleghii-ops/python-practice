# Exercise 6: Check if a key exists in a dictionary

student = {
    "name": "Kourosh Khaleghi",
    "age": 22,
    "student_id": "769291"
}

key_to_check = "age"

if key_to_check in student:
    print(f"Key '{key_to_check}' exists with value: {student[key_to_check]}")
else:
    print(f"Key '{key_to_check}' does not exist.")