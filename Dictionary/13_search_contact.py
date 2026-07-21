# Exercise 13: Search for a contact in phonebook
# way1:
def search_contact(phonebook, name):
    return phonebook.get(name, "Contact not found")
#way2:
def search_contact_manual(phonebook, name):
    if name in phonebook:
        return phonebook[name]
    else:
        return "Contact not found"

# example
phonebook = {"kourosh": "09121111111", "daryoush": "09222222222", "arad": "09333333333"}
name = input("Enter name to search: ")
print("Way 1:", search_contact(phonebook, name))
print("Way 2:", search_contact_manual(phonebook, name))