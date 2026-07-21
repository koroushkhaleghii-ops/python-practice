# Exercise 20: Find the student with the highest grade

def top_student(grades):
    if not grades:
        return None
    top_name = None
    top_score = -1
    for name, score in grades.items():
        if score > top_score:
            top_score = score
            top_name = name
    return top_name

# Example
grades = {"Kourosh": 18, "Bard": 20, "Tom": 15, "Yori": 19}
print(f"Grades: {grades}")
print("Top : ", top_student(grades))