

contacts = []   

while True:
    print("\n--- CONTACT MANAGEMENT MENU ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }

        contacts.append(contact)
        print("Contact added successfully!")

    
    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            print("\nContact List:")
            for i, contact in enumerate(contacts, start=1):
                print(i, ".", contact["name"], "-", contact["phone"])

    
    elif choice == "3":
        search = input("Enter name or phone to search: ")
        found = False

        for contact in contacts:
            if search == contact["name"] or search == contact["phone"]:
                print("\nContact Found:")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("Address:", contact["address"])
                found = True

        if not found:
            print("Contact not found.")

    
    elif choice == "4":
        phone = input("Enter phone number of contact to update: ")
        for contact in contacts:
            if phone == contact["phone"]:
                contact["name"] = input("Enter new name: ")
                contact["email"] = input("Enter new email: ")
                contact["address"] = input("Enter new address: ")
                print("Contact updated successfully!")
                break
        else:
            print("Contact not found.")

    
    elif choice == "5":
        phone = input("Enter phone number of contact to delete: ")
        for contact in contacts:
            if phone == contact["phone"]:
                contacts.remove(contact)
                print("Contact deleted successfully!")
                break
        else:
            print("Contact not found.")

    
    elif choice == "6":
        print("Exiting Contact Management System.")
        break

    else:
        print("Invalid choice! Please try again.")
