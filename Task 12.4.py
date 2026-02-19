with open("files/contacts.txt", encoding="utf-8") as file:
    contacts_read = file.readlines()
    contacts_clean = [line.rstrip('\n').split(":") for line in contacts_read]
    contacts = {}
    for con in contacts_clean:
        contacts[con[0]] = con[1]
    name = input("Enter name to search number: ").strip()
    if name in contacts:
        print(f"{name} -> {contacts[name]}")
    else:
        number = input("There is no one on this name, enter number to add: ")
        contacts[name] = number
    contacts = dict(sorted(contacts.items()))

with open("files/contacts.txt", "w", encoding="utf-8") as file:
    for name, number in contacts.items():
        file.write(f"{name}:{number}\n")