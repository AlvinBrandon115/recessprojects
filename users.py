class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print("User Information")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print()

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.\n")


# Create several users
user1 = User("Alvin", "Brandon", 20, "Kampala")
user2 = User("Sarah", "Namuli", 22, "Jinja")
user3 = User("John", "Kato", 25, "Mbarara")

# Call both methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()