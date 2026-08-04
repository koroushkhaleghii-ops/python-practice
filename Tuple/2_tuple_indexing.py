# Exercise 2: Access tuple elements by index

def access_elements():
    fruits = ("apple", "banana", "cherry", "date")
    print("Tuple:", fruits)
    print("Third element (index 2):", fruits[2])
    print("Last element (index -1):", fruits[-1])

def access_elements_loop():
    fruits = ("apple", "banana", "cherry", "date")
    print("Elements with index:")
    for i in range(len(fruits)):
        print(f"  Index {i}: {fruits[i]}")

# Example
access_elements()
access_elements_loop()