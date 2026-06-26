# Parent Class
class Transaction:
    def process_transaction(self):
        print("Processing transaction...")


# Child Class: Deposit
class Deposit(Transaction):
    # Method Overloading (simulated using default argument)
    def deposit(self, amount, bonus=0):
        total = amount + bonus
        print(f"Deposited UGX {total:,}")

    # Method Overriding
    def process_transaction(self):
        print("Deposit transaction processed.")


# Child Class: Withdrawal
class Withdrawal(Transaction):
    def withdraw(self, amount):
        print(f"Withdrawn UGX {amount:,}")

    # Method Overriding
    def process_transaction(self):
        print("Withdrawal transaction processed.")


# Child Class: Transfer
class Transfer(Transaction):
    def transfer(self, amount, recipient):
        print(f"Transferred UGX {amount:,} to {recipient}")

    # Method Overriding
    def process_transaction(self):
        print("Transfer transaction processed.")


# Demonstration
print("=== Employer Banking System ===")

# Deposit
emp_deposit = Deposit()
emp_deposit.process_transaction()
emp_deposit.deposit(500000)          # Normal deposit
emp_deposit.deposit(500000, 50000)   # Overloaded version with bonus

print()

# Withdrawal
emp_withdraw = Withdrawal()
emp_withdraw.process_transaction()
emp_withdraw.withdraw(200000)

print()

# Transfer
emp_transfer = Transfer()
emp_transfer.process_transaction()
emp_transfer.transfer(150000, "John Doe")