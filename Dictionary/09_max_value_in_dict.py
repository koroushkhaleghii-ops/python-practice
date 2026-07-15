# Exercise 9: Find the maximum value in a dictionary

scores = {
    "kourosh": 18,
    "ali": 20,
    "reza": 15,
    "sam": 19
}

max_value = max(scores.values())
print("Maximum score:", max_value)

max_key = max(scores, key=scores.get)
print("Student with max score:", max_key, "->", scores[max_key])