# Custom Exception
class UnderAgeError(Exception):
    def __init__(self, message="Must be 18 years or older to drive in Uganda."):
        self.message = message
        super().__init__(self.message)


# Function to check eligibility
def check_driver_age(age):
    if age < 18:
        raise UnderAgeError
    else:
        print("You are eligible to drive a car in Uganda.")


# Main Program
try:
    age = int(input("Enter your age: "))
    check_driver_age(age)

except UnderAgeError as e:
    print("Error:", e)

except ValueError:
    print("Please enter a valid number for age.")