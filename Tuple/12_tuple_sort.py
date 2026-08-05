# Exercise 12: Sort a tuple (return new sorted tuple)

def sort_simple():
    numbers = (5, 2, 8, 1, 9)
    sorted_tuple = tuple(sorted(numbers))
    print("Original:", numbers)
    print("Sorted ascending:", sorted_tuple)
    sorted_desc = tuple(sorted(numbers, reverse=True))
    print("Sorted descending:", sorted_desc)

def sort_manual():
    numbers = (5, 2, 8, 1, 9)
    lst = list(numbers)
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    sorted_manual = tuple(lst)
    print("Manual sort:", sorted_manual)

# Example
sort_simple()
sort_manual()