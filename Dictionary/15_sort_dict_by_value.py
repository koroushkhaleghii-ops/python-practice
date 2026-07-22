# Exercise 18: Sort a dictionary by its values (concept)


def sort_by_value_manual(d):
    items = list(d.items())
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i][1] > items[j][1]:
                items[i], items[j] = items[j], items[i]
    return dict(items)

# example
scores = {"kourosh": 18, "samir": 20, "arta": 15, "john": 19}
print("Original:", scores)
print("Sorted by value :", sort_by_value_manual(scores))

