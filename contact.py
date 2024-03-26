class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
class ContactBook:
    def __init__(self):
        self.contacts = []
    def add_contact(self, contact):
        self.contacts.append(contact)
    def view_contact_list(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone_number}")
    def search_contact(self, search_query):
        for contact in self.contacts:
            if search_query.lower() in contact.name.lower() or search_query in contact.phone_number:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")
    def update_contact(self, name, new_phone_number=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_phone_number:
                    contact.phone_number = new_phone_number
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"{name} has been deleted from contacts.")
def main():
    contact_book = ContactBook()
    while True:
        print("\n Contact Management System ")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)
            print("Contact added successfully.")
        elif choice == '2':
            print("\n Contact List ")
            contact_book.view_contact_list()
        elif choice == '3':
            search_query = input("Enter name or phone number to search: ")
            print("\n Search Results ")
            contact_book.search_contact(search_query)
        elif choice == '4':
            name = input("Enter name of contact to update: ")
            new_phone_number = input("Enter new phone number (press enter to skip): ")
            new_email = input("Enter new email (press enter to skip): ")
            new_address = input("Enter new address (press enter to skip): ")
            contact_book.update_contact(name, new_phone_number, new_email, new_address)
            print("Contact updated successfully.")
        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()