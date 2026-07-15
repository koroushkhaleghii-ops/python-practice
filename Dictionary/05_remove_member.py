# Exercise 5: Remove a member from a dictionary

student = {
    "name": "Kourosh Khaleghi",
    "age": 22,
    "student_id": "3844819",
    "grade": 18.5
}

print("Before removal:", student)


removed_value = student.pop("grade", None)
print("Removed value:", removed_value)

print("After removal:", student)
