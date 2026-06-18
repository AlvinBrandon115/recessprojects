import re

class ContactManager:
    def __init__(self):
        """Initialize the contact manager with an empty list of contacts"""
        self.contacts = []
    
    def validate_phone(self, phone):
        """
        Validate phone number: only digits and hyphens allowed
        Returns True if valid, False otherwise
        """
        # Allow digits, hyphens, and plus sign at start
        pattern = r'^[\+\d\-]+$'
        if re.match(pattern, phone):
            return True
        return False
    
    def validate_email(self, email):
        """
        Validate email: must contain @ and a period
        Returns True if valid, False otherwise
        """
        if '@' in email and '.' in email:
            return True
        return False
    
    def add_contact(self, name, phone, email):
        """
        Add a new contact with validation
        
        Args:
            name (str): Contact name
            phone (str): Phone number
            email (str): Email address
        
        Returns:
            bool: True if contact was added successfully, False otherwise
        """
        # Check if name already exists
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                print(f"Error: Contact '{name}' already exists!")
                return False
        
        # Validate phone number
        if not self.validate_phone(phone):
            print("Error: Invalid phone number. Phone numbers can only contain digits, hyphens, and a leading plus sign.")
            return False
        
        # Validate email (if provided)
        if email and not self.validate_email(email):
            print("Error: Invalid email address. Email must contain '@' and a period (.)")
            return False
        
        # Add the contact
        contact = {
            'name': name,
            'phone': phone,
            'email': email
        }
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully!")
        return True
    
    def view_contact(self, name):
        """
        View a specific contact by name
        
        Args:
            name (str): Contact name to view
        
        Returns:
            dict or None: Contact details if found, None otherwise
        """
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                return contact
        print(f"Contact '{name}' not found.")
        return None
    
    def update_contact(self, name, new_phone=None, new_email=None):
        """
        Update an existing contact's phone and/or email with validation
        
        Args:
            name (str): Name of contact to update
            new_phone (str, optional): New phone number
            new_email (str, optional): New email address
        
        Returns:
            bool: True if contact was updated successfully, False otherwise
        """
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                # Validate new phone if provided
                if new_phone:
                    if not self.validate_phone(new_phone):
                        print("Error: Invalid phone number. Phone numbers can only contain digits, hyphens, and a leading plus sign.")
                        return False
                    contact['phone'] = new_phone
                
                # Validate new email if provided
                if new_email:
                    if not self.validate_email(new_email):
                        print("Error: Invalid email address. Email must contain '@' and a period (.)")
                        return False
                    contact['email'] = new_email
                
                print(f"Contact '{name}' updated successfully!")
                return True
        
        print(f"Contact '{name}' not found.")
        return False
    
    def delete_contact(self, name):
        """
        Delete a contact by name
        
        Args:
            name (str): Name of contact to delete
        
        Returns:
            bool: True if contact was deleted successfully, False otherwise
        """
        for i, contact in enumerate(self.contacts):
            if contact['name'].lower() == name.lower():
                del self.contacts[i]
                print(f"Contact '{name}' deleted successfully!")
                return True
        
        print(f"Contact '{name}' not found.")
        return False
    
    def search_contacts(self, search_term):
        """
        Search for contacts by name, phone, or email
        
        Args:
            search_term (str): Search term to look for
        
        Returns:
            list: List of matching contacts
        """
        results = []
        search_lower = search_term.lower()
        
        for contact in self.contacts:
            if (search_lower in contact['name'].lower() or 
                search_lower in contact['phone'].lower() or 
                search_lower in contact['email'].lower()):
                results.append(contact)
        
        return results
    
    def list_all_contacts(self):
        """
        List all contacts in a formatted manner
        
        Returns:
            list: All contacts
        """
        return self.contacts
    
    def format_contact(self, contact, index=None):
        """
        Format a single contact for display
        
        Args:
            contact (dict): Contact to format
            index (int, optional): Index number to display
        
        Returns:
            str: Formatted contact string
        """
        if index is not None:
            header = f"#{index} "
        else:
            header = ""
        
        return (f"{header}Name: {contact['name']}\n"
                f"   Phone: {contact['phone']}\n"
                f"   Email: {contact['email'] if contact['email'] else 'N/A'}")


def display_contact_list(contacts, title="Search Results"):
    """
    Display a list of contacts in a clean format
    
    Args:
        contacts (list): List of contacts to display
        title (str): Title to display above the results
    """
    if not contacts:
        print(f"\n=== {title} ===")
        print("-" * 40)
        print("No contacts found.")
        return
    print(f"\n=== {title} ===")
    print("-" * 40)
    for i, contact in enumerate(contacts, 1):
        print(f"\nContact #{i}:")
        print(f"  Name: {contact['name']}")
        print(f"  Phone: {contact['phone']}")
        print(f"  Email: {contact['email'] if contact['email'] else 'N/A'}")
        print("-" * 40)


def main():
    """Main interactive CLI loop for the contact manager"""
    manager = ContactManager()
    
    print("\n" + "="*50)
    print("WELCOME TO CONTACT MANAGER".center(50))
    print("="*50)
    
    while True:
        print("\n=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ").strip()
        
        # Add Contact
        if choice == '1':
            print("\n--- Add New Contact ---")
            name = input("Enter name: ").strip()
            if not name:
                print("Error: Name cannot be empty.")
                continue
            
            phone = input("Enter phone number: ").strip()
            if not phone:
                print("Error: Phone number cannot be empty.")
                continue
            
            email = input("Enter email (press Enter to skip): ").strip()
            
            manager.add_contact(name, phone, email)
        
        # View Contact
        elif choice == '2':
            print("\n--- View Contact ---")
            name = input("Enter contact name: ").strip()
            contact = manager.view_contact(name)
            if contact:
                print("\nContact Details:")
                print("-" * 30)
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email'] if contact['email'] else 'N/A'}")
                print("-" * 30)
        
        # Update Contact
        elif choice == '3':
            print("\n--- Update Contact ---")
            name = input("Enter contact name to update: ").strip()
            if not name:
                print("Error: Name cannot be empty.")
                continue
            
            # Check if contact exists first
            contact = manager.view_contact(name)
            if not contact:
                continue
            
            print(f"Current phone: {contact['phone']}")
            new_phone = input("Enter new phone number (press Enter to keep current): ").strip()
            if not new_phone:
                new_phone = None
            
            print(f"Current email: {contact['email'] if contact['email'] else 'N/A'}")
            new_email = input("Enter new email (press Enter to keep current): ").strip()
            if not new_email:
                new_email = None
            
            manager.update_contact(name, new_phone, new_email)
        
        # Delete Contact
        elif choice == '4':
            print("\n--- Delete Contact ---")
            name = input("Enter contact name to delete: ").strip()
            if not name:
                print("Error: Name cannot be empty.")
                continue
            
            # Confirm deletion
            confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").strip().lower()
            if confirm in ['y', 'yes']:
                manager.delete_contact(name)
            else:
                print("Deletion cancelled.")
        
        # Search Contacts
        elif choice == '5':
            print("\n--- Search Contacts ---")
            search_term = input("Enter search term (name, phone, or email): ").strip()
            if not search_term:
                print("Error: Search term cannot be empty.")
                continue
            
            results = manager.search_contacts(search_term)
            display_contact_list(results, f"Search Results for '{search_term}'")
        
        # List All Contacts
        elif choice == '6':
            print("\n--- All Contacts ---")
            all_contacts = manager.list_all_contacts()
            display_contact_list(all_contacts, "Contact List")
            print(f"\nTotal contacts: {len(all_contacts)}")
            input("\nPress Enter to return to the menu...")
        
        # Exit
        elif choice == '7':
            print("\nThank you for using Contact Manager!")
            print("Goodbye!")
            break
        
        # Invalid option
        else:
            print("Invalid option. Please choose a number between 1 and 7.")


if __name__ == "__main__":
    main()