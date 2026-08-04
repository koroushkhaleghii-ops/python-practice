# Exercise 1: Create a tuple and print its elements

def create_and_print():
    person = ("Ali", 25, "Tehran")
    print("Tuple:", person)
    print("Elements:")
    for item in person:
        print(f"  {item}")

# Example
create_and_print()