# Exercise 3: Check membership in a set

def membership_in():
    colors = {"red", "green", "blue"}
    print("Set:", colors)
    print("'green' in set:", "green" in colors)
    print("'yellow' in set:", "yellow" in colors)

def membership_loop():
    colors = {"red", "green", "blue"}
    target = "green"
    found = False
    for color in colors:
        if color == target:
            found = True
            break
    print(f"'{target}' found manually:", found)

# Example
membership_in()
membership_loop()