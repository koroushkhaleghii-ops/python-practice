# Exercise 20: Convert tuple to list, modify, convert back

def modify_via_list():
    original = (1, 2, 3, 4)
    print("Original tuple:", original)
    temp_list = list(original)
    temp_list.append(5)
    temp_list.remove(2)
    modified = tuple(temp_list)
    print("Modified tuple:", modified)

def modify_manual():
    original = (1, 2, 3, 4)
    modified = original + (5,)
    modified = tuple(x for x in modified if x != 2)
    print("Manual modification:", modified)

# Example
modify_via_list()
modify_manual()