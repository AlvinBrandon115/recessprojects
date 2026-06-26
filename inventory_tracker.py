import re
from datetime import datetime

class InventoryTracker:
    def __init__(self):
        """Initialize the inventory tracker with an empty list of items"""
        self.inventory = []
        self.transaction_history = []
    
    def validate_sku(self, sku):
        """
        Validate SKU: must be alphanumeric with optional hyphens
        Returns True if valid, False otherwise
        """
        pattern = r'^[A-Za-z0-9\-]+$'
        if re.match(pattern, sku):
            return True
        return False
    
    def validate_price(self, price):
        """
        Validate price: must be a positive number
        Returns True if valid, False otherwise
        """
        try:
            price_float = float(price)
            if price_float >= 0:
                return True
            return False
        except ValueError:
            return False
    
    def validate_quantity(self, quantity):
        """
        Validate quantity: must be a non-negative integer
        Returns True if valid, False otherwise
        """
        try:
            qty_int = int(quantity)
            if qty_int >= 0:
                return True
            return False
        except ValueError:
            return False
    
    def add_item(self, sku, name, quantity, price, category=""):
        """
        Add a new item to inventory with validation
        
        Args:
            sku (str): Stock Keeping Unit (unique identifier)
            name (str): Item name
            quantity (int): Initial quantity
            price (float): Item price
            category (str): Item category (optional)
        
        Returns:
            bool: True if item was added successfully, False otherwise
        """
        # Check if SKU already exists
        for item in self.inventory:
            if item['sku'].lower() == sku.lower():
                print(f"Error: Item with SKU '{sku}' already exists!")
                return False
        
        # Validate SKU
        if not self.validate_sku(sku):
            print("Error: Invalid SKU. SKU can only contain letters, numbers, and hyphens.")
            return False
        
        # Validate quantity
        if not self.validate_quantity(quantity):
            print("Error: Invalid quantity. Quantity must be a non-negative integer.")
            return False
        
        # Validate price
        if not self.validate_price(price):
            print("Error: Invalid price. Price must be a positive number.")
            return False
        
        # Add the item
        item = {
            'sku': sku.upper(),
            'name': name,
            'quantity': int(quantity),
            'price': float(price),
            'category': category,
            'date_added': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.inventory.append(item)
        
        # Log transaction
        self._log_transaction('ADD', sku.upper(), name, int(quantity))
        print(f"Item '{name}' (SKU: {sku.upper()}) added successfully!")
        return True
    
    def view_item(self, sku):
        """
        View a specific item by SKU
        
        Args:
            sku (str): Item SKU to view
        
        Returns:
            dict or None: Item details if found, None otherwise
        """
        for item in self.inventory:
            if item['sku'].lower() == sku.lower():
                return item
        print(f"Item with SKU '{sku}' not found.")
        return None
    
    def update_item(self, sku, name=None, quantity=None, price=None, category=None):
        """
        Update an existing item with validation
        
        Args:
            sku (str): SKU of item to update
            name (str, optional): New item name
            quantity (int, optional): New quantity
            price (float, optional): New price
            category (str, optional): New category
        
        Returns:
            bool: True if item was updated successfully, False otherwise
        """
        for item in self.inventory:
            if item['sku'].lower() == sku.lower():
                # Validate and update name
                if name:
                    item['name'] = name
                
                # Validate and update quantity
                if quantity is not None:
                    if not self.validate_quantity(quantity):
                        print("Error: Invalid quantity. Quantity must be a non-negative integer.")
                        return False
                    new_qty = int(quantity)
                    old_qty = item['quantity']
                    item['quantity'] = new_qty
                    
                    # Log quantity change if different
                    if new_qty != old_qty:
                        self._log_transaction('UPDATE_QTY', sku.upper(), item['name'], new_qty - old_qty)
                
                # Validate and update price
                if price is not None:
                    if not self.validate_price(price):
                        print("Error: Invalid price. Price must be a positive number.")
                        return False
                    item['price'] = float(price)
                
                # Update category
                if category is not None:
                    item['category'] = category
                
                item['last_updated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"Item '{item['name']}' (SKU: {sku.upper()}) updated successfully!")
                return True
        
        print(f"Item with SKU '{sku}' not found.")
        return False
    
    def delete_item(self, sku):
        """
        Delete an item by SKU
        
        Args:
            sku (str): SKU of item to delete
        
        Returns:
            bool: True if item was deleted successfully, False otherwise
        """
        for i, item in enumerate(self.inventory):
            if item['sku'].lower() == sku.lower():
                item_name = item['name']
                del self.inventory[i]
                self._log_transaction('DELETE', sku.upper(), item_name, 0)
                print(f"Item '{item_name}' (SKU: {sku.upper()}) deleted successfully!")
                return True
        
        print(f"Item with SKU '{sku}' not found.")
        return False
    
    def search_items(self, search_term):
        """
        Search for items by SKU, name, or category
        
        Args:
            search_term (str): Search term to look for
        
        Returns:
            list: List of matching items
        """
        results = []
        search_lower = search_term.lower()
        
        for item in self.inventory:
            if (search_lower in item['sku'].lower() or 
                search_lower in item['name'].lower() or 
                search_lower in item['category'].lower()):
                results.append(item)
        
        return results
    
    def list_all_items(self):
        """
        List all items in inventory
        
        Returns:
            list: All inventory items
        """
        return self.inventory
    
    def get_low_stock_items(self, threshold=5):
        """
        Get items with quantity below threshold
        
        Args:
            threshold (int): Quantity threshold
        
        Returns:
            list: Items with low stock
        """
        low_stock = []
        for item in self.inventory:
            if item['quantity'] <= threshold:
                low_stock.append(item)
        return low_stock
    
    def get_total_inventory_value(self):
        """
        Calculate total value of all inventory
        
        Returns:
            float: Total inventory value
        """
        total = sum(item['quantity'] * item['price'] for item in self.inventory)
        return total
    
    def _log_transaction(self, action, sku, name, quantity_change):
        """
        Log a transaction for audit purposes
        
        Args:
            action (str): Transaction type (ADD, UPDATE_QTY, DELETE)
            sku (str): Item SKU
            name (str): Item name
            quantity_change (int): Change in quantity
        """
        transaction = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'action': action,
            'sku': sku,
            'name': name,
            'quantity_change': quantity_change
        }
        self.transaction_history.append(transaction)
    
    def view_transaction_history(self, limit=10):
        """
        View recent transaction history
        
        Args:
            limit (int): Number of recent transactions to show
        """
        if not self.transaction_history:
            print("No transactions recorded.")
            return []
        
        recent = self.transaction_history[-limit:]
        return recent
    
    def format_item(self, item, index=None):
        """
        Format a single item for display
        
        Args:
            item (dict): Item to format
            index (int, optional): Index number to display
        
        Returns:
            str: Formatted item string
        """
        if index is not None:
            header = f"#{index} "
        else:
            header = ""
        
        return (f"{header}SKU: {item['sku']}\n"
                f"   Name: {item['name']}\n"
                f"   Quantity: {item['quantity']}\n"
                f"   Price: ${item['price']:.2f}\n"
                f"   Category: {item['category'] if item['category'] else 'Uncategorized'}\n"
                f"   Last Updated: {item['last_updated']}")


def display_item_list(items, title="Search Results"):
    """
    Display a list of items in a clean format
    
    Args:
        items (list): List of items to display
        title (str): Title to display above the results
    """
    if not items:
        print("No items found.")
        return
    
    print(f"\n{'='*60}")
    print(f"{title.center(60)}")
    print('='*60)
    
    for i, item in enumerate(items, 1):
        print(f"\nItem #{i}:")
        print(f"  SKU: {item['sku']}")
        print(f"  Name: {item['name']}")
        print(f"  Quantity: {item['quantity']}")
        print(f"  Price: ${item['price']:.2f}")
        print(f"  Category: {item['category'] if item['category'] else 'Uncategorized'}")
        print(f"  Added: {item['date_added']}")
        print(f"  Updated: {item['last_updated']}")
        print('-'*60)


def main():
    """Main interactive CLI loop for the inventory tracker"""
    tracker = InventoryTracker()
    
    # Sample data for testing
    sample_items = [
        ("LAP-001", "Laptop Pro", 15, 999.99, "Electronics"),
        ("LAP-002", "Laptop Air", 8, 799.99, "Electronics"),
        ("PHN-001", "Smartphone X", 25, 599.99, "Electronics"),
        ("ACC-001", "Wireless Mouse", 50, 29.99, "Accessories"),
        ("ACC-002", "USB-C Cable", 100, 14.99, "Accessories"),
        ("BAG-001", "Backpack", 12, 49.99, "Bags"),
    ]
    
    for sku, name, qty, price, category in sample_items:
        tracker.add_item(sku, name, qty, price, category)
    
    print("\n" + "="*60)
    print("WELCOME TO INVENTORY TRACKER SYSTEM".center(60))
    print("="*60)
    
    while True:
        print("\n=== Inventory Tracker Menu ===")
        print("1. Add Item")
        print("2. View Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Search Items")
        print("6. List All Items")
        print("7. Check Low Stock Items")
        print("8. View Total Inventory Value")
        print("9. View Transaction History")
        print("10. Exit")
        
        choice = input("Choose an option (1-10): ").strip()
        
        # Add Item
        if choice == '1':
            print("\n--- Add New Item ---")
            sku = input("Enter SKU (e.g., LAP-001): ").strip()
            if not sku:
                print("Error: SKU cannot be empty.")
                continue
            
            name = input("Enter item name: ").strip()
            if not name:
                print("Error: Item name cannot be empty.")
                continue
            
            quantity = input("Enter quantity: ").strip()
            if not quantity:
                print("Error: Quantity cannot be empty.")
                continue
            
            price = input("Enter price: ").strip()
            if not price:
                print("Error: Price cannot be empty.")
                continue
            
            category = input("Enter category (press Enter to skip): ").strip()
            
            tracker.add_item(sku, name, quantity, price, category)
        
        # View Item
        elif choice == '2':
            print("\n--- View Item ---")
            sku = input("Enter item SKU: ").strip()
            item = tracker.view_item(sku)
            if item:
                print("\nItem Details:")
                print('-'*40)
                print(f"SKU: {item['sku']}")
                print(f"Name: {item['name']}")
                print(f"Quantity: {item['quantity']}")
                print(f"Price: ${item['price']:.2f}")
                print(f"Category: {item['category'] if item['category'] else 'Uncategorized'}")
                print(f"Date Added: {item['date_added']}")
                print(f"Last Updated: {item['last_updated']}")
                print('-'*40)
        
        # Update Item
        elif choice == '3':
            print("\n--- Update Item ---")
            sku = input("Enter item SKU to update: ").strip()
            if not sku:
                print("Error: SKU cannot be empty.")
                continue
            
            # Check if item exists first
            item = tracker.view_item(sku)
            if not item:
                continue
            
            print(f"\nCurrent details for {item['name']} (SKU: {item['sku']}):")
            print(f"  Quantity: {item['quantity']}")
            print(f"  Price: ${item['price']:.2f}")
            print(f"  Category: {item['category'] if item['category'] else 'Uncategorized'}")
            
            new_name = input("\nEnter new name (press Enter to keep current): ").strip()
            if not new_name:
                new_name = None
            
            new_quantity = input("Enter new quantity (press Enter to keep current): ").strip()
            if not new_quantity:
                new_quantity = None
            
            new_price = input("Enter new price (press Enter to keep current): ").strip()
            if not new_price:
                new_price = None
            
            new_category = input("Enter new category (press Enter to keep current): ").strip()
            if not new_category:
                new_category = None
            
            tracker.update_item(sku, new_name, new_quantity, new_price, new_category)
        
        # Delete Item
        elif choice == '4':
            print("\n--- Delete Item ---")
            sku = input("Enter item SKU to delete: ").strip()
            if not sku:
                print("Error: SKU cannot be empty.")
                continue
            
            # Check if item exists
            item = tracker.view_item(sku)
            if not item:
                continue
            
            # Confirm deletion
            confirm = input(f"Are you sure you want to delete '{item['name']}' (SKU: {sku})? (y/n): ").strip().lower()
            if confirm in ['y', 'yes']:
                tracker.delete_item(sku)
            else:
                print("Deletion cancelled.")
        
        # Search Items
        elif choice == '5':
            print("\n--- Search Items ---")
            search_term = input("Enter search term (SKU, name, or category): ").strip()
            if not search_term:
                print("Error: Search term cannot be empty.")
                continue
            
            results = tracker.search_items(search_term)
            display_item_list(results, f"Search Results for '{search_term}'")
        
        # List All Items
        elif choice == '6':
            print("\n--- All Inventory Items ---")
            all_items = tracker.list_all_items()
            display_item_list(all_items, "Complete Inventory List")
            print(f"\nTotal items: {len(all_items)}")
            print(f"Total inventory value: ${tracker.get_total_inventory_value():.2f}")
        
        # Low Stock Items
        elif choice == '7':
            print("\n--- Low Stock Items ---")
            threshold = input("Enter stock threshold (default 5): ").strip()
            if not threshold:
                threshold = 5
            else:
                try:
                    threshold = int(threshold)
                except ValueError:
                    print("Invalid threshold. Using default value of 5.")
                    threshold = 5
            
            low_stock = tracker.get_low_stock_items(threshold)
            if low_stock:
                display_item_list(low_stock, f"Low Stock Items (≤ {threshold})")
                print(f"\nTotal low stock items: {len(low_stock)}")
            else:
                print(f"All items have sufficient stock (> {threshold}).")
        
        # Total Inventory Value
        elif choice == '8':
            print("\n--- Total Inventory Value ---")
            total_value = tracker.get_total_inventory_value()
            print(f"Total inventory value: ${total_value:.2f}")
            
            # Show breakdown
            if tracker.inventory:
                print("\nBreakdown by item:")
                print("-"*40)
                for item in tracker.inventory:
                    value = item['quantity'] * item['price']
                    print(f"{item['sku']}: {item['name']} - ${value:.2f}")
        
        # Transaction History
        elif choice == '9':
            print("\n--- Transaction History ---")
            limit = input("Enter number of recent transactions to view (default 10): ").strip()
            if not limit:
                limit = 10
            else:
                try:
                    limit = int(limit)
                except ValueError:
                    print("Invalid input. Using default of 10.")
                    limit = 10
            
            history = tracker.view_transaction_history(limit)
            if history:
                print("\nRecent Transactions:")
                print('='*60)
                for trans in history:
                    print(f"\n{trans['timestamp']}")
                    print(f"  Action: {trans['action']}")
                    print(f"  SKU: {trans['sku']}")
                    print(f"  Name: {trans['name']}")
                    if trans['quantity_change'] != 0:
                        print(f"  Quantity Change: {trans['quantity_change']:+d}")
                    print('-'*60)
        
        # Exit
        elif choice == '10':
            print("\nThank you for using Inventory Tracker System!")
            print("Goodbye!")
            break
        
        # Invalid option
        else:
            print("Invalid option. Please choose a number between 1 and 10.")


if __name__ == "__main__":
    main()