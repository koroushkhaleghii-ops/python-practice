# Exercise 14: Delete a contact from phonebook
#way1:
def delete_contact_pop(phonebook, name):
    removed = phonebook.pop(name, None)
    if removed:
        print(f"Removed {name}: {removed}")
    else:
        print(f"{name} not found")
    return phonebook
#way2:
def delete_contact_manual(phonebook, name):
    if name in phonebook:
        del phonebook[name]
        print(f"Removed {name}")
    else:
        print(f"{name} not found")
    return phonebook

# example
phonebook = {"rodi": "09121134211", "kourosh": "0924325222", "tali": "09333432497"}
name = input("Enter name to delete: ")
print("Before:", phonebook)
delete_contact_pop(phonebook, name)
print("After:", phonebook)