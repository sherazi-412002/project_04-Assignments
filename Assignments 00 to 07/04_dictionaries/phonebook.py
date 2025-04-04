
def read_phone_numbers():
    contacts = {}
    while True:
        name = input("Name (Press Enter to Exit!) : ").strip()
        if name == "":
            break
        number = input("Number : ").strip()
        contacts[name] = number

    return contacts

def print_contacts(contacts):
    for name1 in contacts:
        print(str(name1)+ " -> " + contacts[name1])


def look_up_contacts(contacts):
    while True:
        name = input("Enter a name to lookup (Press Enter to Exit!): ").strip()
        if name == "":
            break
        elif not name in contacts:
            print(f"{name} is not in Contacts!")
        else:
            print(str(name) + "--> " + contacts[name])

def main():
    contacts = read_phone_numbers()
    print_contacts(contacts)
    look_up_contacts(contacts)


if __name__ == "__main__":
    main()