# Exercise 3: Calculate the class average from a dictionary of student grades

def average_grades_builtin(grades_dict):
    if not grades_dict:
        return None
    total = sum(grades_dict.values())
    return total / len(grades_dict)

def average_grades_manual(grades_dict):
    if not grades_dict:
        return None
    total = 0
    count = 0
    for grade in grades_dict.values():
        total += grade
        count += 1
    return total / count

# Example
grades = {
    "kourosh": 18,
    "ali": 20,
    "reza": 15,
    "kanye": 19,
    "molly": 17
}
print(f"Grades: {grades}")
print("Using built-in sum/len:", average_grades_builtin(grades))
print("Using manual loop:", average_grades_manual(grades))