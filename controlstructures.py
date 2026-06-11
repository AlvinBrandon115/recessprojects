# ==========================================
# E-COMMERCE SYSTEM WITH LOGIN
# ==========================================

import getpass
from datetime import datetime

# Store purchase history
purchase_history = []

print("=" * 50)
print("      WELCOME TO PYTHON E-COMMERCE")
print("=" * 50)

# User database
users = {
    "admin": {
        "password": "admin123",
        "role": "Admin"
    },
    "customer": {
        "password": "customer123",
        "role": "Customer"
    },
    "cashier": {
        "password": "cashier123",
        "role": "Cashier"
    }
}

# Keep trying until successful login or user gives up
login_successful = False

while not login_successful:
    # Login
    username = input("\nEnter username: ").lower()
    password = getpass.getpass("Enter password: ")
    
    if username in users:
        if users[username]["password"] == password:
            role = users[username]["role"]
            login_successful = True
            
            print(f"\nLogin successful!")
            print(f"Welcome, {role}")
            
            # Show access level
            if role == "Admin":
                print("Access Level: Full Access")
                # Show all users if admin
                print("\nRegistered Users:")
                for user in users:
                    print(f"  - {user} ({users[user]['role']})")
                    
            elif role == "Cashier":
                print("Access Level: Sales & Transactions")
            elif role == "Customer":
                print("Access Level: Purchase Only")
            
            print("\n" + "=" * 50)
            print("         PRODUCT CHECKOUT")
            print("=" * 50)
            
            # Get subtotal with validation
            while True:
                try:
                    subtotal = float(input("Enter subtotal amount ($): "))
                    if subtotal <= 0:
                        print("Subtotal must be greater than 0.")
                    else:
                        break
                except ValueError:
                    print("Please enter a valid number.")
            
            # Calculate discount based on amount
            discount_percent = 0
            if subtotal >= 1000:
                discount_percent = 20
            elif subtotal >= 500:
                discount_percent = 10
            elif subtotal >= 200:
                discount_percent = 5
            
            # Coupon code
            coupon_code = input("\nEnter coupon code (or press Enter to skip): ").upper()
            extra_discount = 0
            
            if coupon_code != "":
                if coupon_code == "SAVE10":
                    extra_discount = 10
                    print("Coupon Applied: 10% OFF")
                elif coupon_code == "SAVE20":
                    if subtotal >= 500:
                        extra_discount = 20
                        print("Coupon Applied: 20% OFF")
                    else:
                        print("SAVE20 only works for purchases above $500.")
                else:
                    print("Invalid coupon code!")
            
            # Calculate discounts
            subtotal_discount = subtotal * discount_percent / 100
            price_after_tier = subtotal - subtotal_discount
            coupon_discount = price_after_tier * extra_discount / 100
            total_discount = subtotal_discount + coupon_discount
            discounted_price = subtotal - total_discount
            
            # Location selection
            print("\nLocations:")
            print("1. Uganda")
            print("2. Kenya")
            print("3. Tanzania")
            
            location = input("Select location (1-3): ")
            
            tax_rate = 0
            country = ""
            
            if location == "1":
                tax_rate = 18
                country = "Uganda"
            elif location == "2":
                tax_rate = 16
                country = "Kenya"
            elif location == "3":
                tax_rate = 18
                country = "Tanzania"
            else:
                print("Invalid location selected. Default tax = 10%")
                tax_rate = 10
                country = "Unknown"
            
            # Calculate tax
            tax_amount = discounted_price * tax_rate / 100
            final_price = discounted_price + tax_amount
            
            # Payment method
            print("\nPayment Methods:")
            print("1. Credit Card (2% fee)")
            print("2. Mobile Money (1% fee)")
            print("3. Bank Transfer (0% fee)")
            
            payment_choice = input("Select payment method (1-3): ")
            payment_fee = 0
            payment_name = ""
            
            if payment_choice == "1":
                payment_fee = final_price * 0.02
                payment_name = "Credit Card"
            elif payment_choice == "2":
                payment_fee = final_price * 0.01
                payment_name = "Mobile Money"
            elif payment_choice == "3":
                payment_fee = 0
                payment_name = "Bank Transfer"
            else:
                payment_name = "Unknown"
                print("Invalid selection, using default")
            
            final_price = final_price + payment_fee
            
            # Save to purchase history
            purchase_record = {
                "user": username,
                "role": role,
                "amount": final_price,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "country": country,
                "payment": payment_name
            }
            purchase_history.append(purchase_record)
            
            # Calculate customer total if needed
            if role == "Customer":
                customer_total = 0
                for transaction in purchase_history:
                    if transaction['user'] == username:
                        customer_total = customer_total + transaction['amount']
            
            # Display receipt
            print("\n" + "=" * 50)
            print("            E-COMMERCE RECEIPT")
            print("=" * 50)
            
            print(f"User Role:             {role}")
            print(f"Location:              {country}")
            print(f"Subtotal:              ${subtotal:.2f}")
            print(f"Discount Level:        {discount_percent}%")
            
            if extra_discount > 0:
                print(f"Coupon Discount:       {extra_discount}%")
            
            print(f"Total Discount:        ${total_discount:.2f}")
            print(f"Price After Discount:  ${discounted_price:.2f}")
            print(f"Tax Rate:              {tax_rate}%")
            print(f"Tax Amount:            ${tax_amount:.2f}")
            print(f"Payment Method:        {payment_name}")
            
            if payment_fee > 0:
                print(f"Payment Fee:           ${payment_fee:.2f}")
            
            print(f"Final Price:           ${final_price:.2f}")
            
            if role == "Customer":
                print(f"Your total today:      ${customer_total:.2f}")
            
            print("=" * 50)
            print("Thank you for shopping!")
            print("=" * 50)
            
            # Show session summary for admin/cashier
            if role == "Admin" or role == "Cashier":
                if len(purchase_history) > 0:
                    print("\n" + "=" * 50)
                    print("      SESSION TRANSACTIONS")
                    print("=" * 50)
                    
                    session_total = 0
                    for i in range(len(purchase_history)):
                        transaction = purchase_history[i]
                        print(f"{i+1}. {transaction['user']} - ${transaction['amount']:.2f} ({transaction['payment']})")
                        session_total = session_total + transaction['amount']
                    
                    print(f"\nTotal Sales: ${session_total:.2f}")
                    print("=" * 50)
            
        else:
            print("Incorrect password! Try again.")
    else:
        # User not found - offer registration
        print("User not found!")
        register = input("Would you like to register? (y/n): ").lower()
        if register == 'y':
            new_user = input("Enter new username: ").lower()
            new_pass = getpass.getpass("Enter password: ")
            confirm_pass = getpass.getpass("Confirm password: ")
            
            if new_pass == confirm_pass:
                users[new_user] = {
                    "password": new_pass,
                    "role": "Customer"
                }
                print(f"\nRegistration successful! Welcome {new_user}!")
                print("Please login with your new credentials.")
                # Continue the loop to let them login
            else:
                print("Passwords do not match. Registration failed.")
                print("Please try logging in again.")
        else:
            print("Okay, goodbye!")
            break  # Exit if they don't want to register

# Show all transactions at the end if there are any
if len(purchase_history) > 0:
    print("\n" + "=" * 50)
    print("      ALL TRANSACTIONS HISTORY")
    print("=" * 50)
    
    total_revenue = 0
    for transaction in purchase_history:
        print(f"{transaction['date']} - {transaction['user']} - ${transaction['amount']:.2f} - {transaction['country']}")
        total_revenue = total_revenue + transaction['amount']
    
    print(f"\nTotal Revenue: ${total_revenue:.2f}")
    print(f"Total Transactions: {len(purchase_history)}")
    print("=" * 50)

print("\nProgram ended.")