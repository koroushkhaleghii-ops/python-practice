# Exercise 3: Create a phonebook dictionary

def create_phonebook():
    phonebook = {}
    while True:
        name = input("Enter name (or 'quit' to exit): ").strip()
        if name.lower() == 'quit':
            break
        if name in phonebook:
            print(f"{name} already exists with number {phonebook[name]}")
            continue
        number = input(f"Enter phone number for {name}: ").strip()
        phonebook[name] = number
        print(f"Added {name}: {number}")
    return phonebook

# example
phonebook = create_phonebook()
print("\nFinal phonebook:")
for name, number in phonebook.items():
    print(f"{name}: {number}")