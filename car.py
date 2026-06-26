class Car:
    def __init__(self, brand, model, price):
        self.brand = brand          # Public attribute
        self._model = model         # Protected attribute (single underscore)
        self.__price = price        # Private attribute (double underscore)
    
    def display_info(self):
        """Display all car information"""
        print(f"Brand: {self.brand}")
        print(f"Model: {self._model}")
        print(f"Price: ${self.__price:,.2f}")

car1=Car("Toyota", "Camry", 25000)
car1.display_info()        