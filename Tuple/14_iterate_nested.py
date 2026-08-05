# Exercise 14: Iterate over nested tuple

def iterate_simple():
    matrix = ((1, 2), (3, 4), (5, 6))
    print("Matrix:")
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()

def iterate_with_index():
    matrix = ((1, 2), (3, 4), (5, 6))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f"matrix[{i}][{j}] = {matrix[i][j]}")

# Example
iterate_simple()
iterate_with_index()