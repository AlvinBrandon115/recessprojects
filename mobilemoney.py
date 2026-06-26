class MobileMoney:
    def __init__(self):
        self.__balance = 0  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        return self.__balance


# Testing the application
acc = MobileMoney()

acc.deposit(500000)
acc.deposit(100000)

print("Current Balance:", acc.check_balance())

acc.withdraw(200000)

print("Balance After Withdrawal:", acc.check_balance())