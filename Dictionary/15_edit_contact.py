# Exercise 15: Edit a contact (change phone number)

def edit_contact(phonebook, name, new_number):
    if name in phonebook:
        phonebook[name] = new_number
        print(f"Updated {name}: {new_number}")
    else:
        print(f"{name} not found")
    return phonebook

# example
phonebook = {"kourosh": "09324325566", "youri": "09765341122"}
print("Before:", phonebook)
name = input("Enter name to edit: ")
new_num = input("Enter new phone number: ")
edit_contact(phonebook, name, new_num)
print("After:", phonebook)