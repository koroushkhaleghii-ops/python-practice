# Exercise 5: Find the index of a value in a tuple

def index_builtin():
    colors = ("red", "green", "blue", "green", "yellow")
    print("Tuple:", colors)
    print("Index of 'green' using index():", colors.index("green"))

def index_manual():
    colors = ("red", "green", "blue", "green", "yellow")
    target = "green"
    index = -1
    for i, color in enumerate(colors):
        if color == target:
            index = i
            break
    print(f"Index of '{target}' using manual loop:", index)

# Example
index_builtin()
index_manual()