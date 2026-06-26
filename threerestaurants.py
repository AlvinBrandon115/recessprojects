class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print()


# Create three instances
restaurant1 = Restaurant("Taste Palace", "African")
restaurant2 = Restaurant("Pizza Hub", "Italian")
restaurant3 = Restaurant("Dragon Wok", "Chinese")

# Call method for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()