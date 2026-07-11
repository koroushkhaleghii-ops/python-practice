"""
Goal: Design a `Student` class that:
1. Has attributes: `name`, `student_id`, and a list of `grades`.
2. Has an `add_grade` method to add a new grade.
3. Has an `average` method to calculate the GPA.
4. Has a `status` method that returns "Passed" if average >= 12, else "Failed".
5. Has a `__str__` magic method to print a clean summary of the student.

"""

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []  # List of grades (0 to 20)

    def add_grade(self, grade):
        if 0 <= grade <= 20:
            self.grades.append(grade)
        else:
            print("Grade must be between 0 and 20.")

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def status(self):
        return "Passed" if self.average() >= 12 else "Failed"

    def __str__(self):
        return f"Student: {self.name} (ID: {self.student_id}) - GPA: {self.average():.2f} - Status: {self.status()}"

# Testing the class
s1 = Student("Ali Rezaei", "9823100")
s1.add_grade(18)
s1.add_grade(14)
s1.add_grade(9)
print(s1)  # The __str__ method is automatically called here