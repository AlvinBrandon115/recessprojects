# Question 1: Print the value of shoe size
print("Question 1:")
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(Shoes["size"])
print("-" * 30)

# Question 2: Change "Nick" to "Adidas"
print("Question 2:")
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
Shoes["brand"] = "Adidas"
print(Shoes)
print("-" * 30)

# Question 3: Add key/value pair "type": "sneakers"
print("Question 3:")
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
Shoes["type"] = "sneakers"
print(Shoes)
print("-" * 30)

# Question 4: Return a list of all keys
print("Question 4:")
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(list(Shoes.keys()))
print("-" * 30)

# Question 5: Return a list of all values
print("Question 5:")
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(list(Shoes.values()))
print("-" * 30)

# Question 6: Check if key "size" exists
print("Question 6:")
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
if "size" in Shoes:
    print("True")
else:
    print("False")
print("-" * 30)

# Question 7: Loop through the dictionary
print("Question 7:")
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
for key, value in Shoes.items():
    print(key + ": " + str(value))
print("-" * 30)

# Question 8: Remove "color" from the dictionary
print("Question 8:")
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
del Shoes["color"]
print(Shoes)
print("-" * 30)

# Question 9: Empty the dictionary
print("Question 9:")
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
Shoes.clear()
print(Shoes)
print("-" * 30)

# Question 10: Create a dictionary and make a copy
print("Question 10:")
my_dict = {
    "name": "John",
    "age": 25,
    "city": "Kampala"
}
my_dict_copy = my_dict.copy()
print(my_dict_copy)
print("-" * 30)

# Question 11: Nested dictionary
print("Question 11:")
nested_dict = {
    "student1": {
        "name": "Alvin",
        "age": 20,
        "course": "Computer Science"
    },
    "student2": {
        "name": "John",
        "age": 22,
        "course": "Information Technology"
    }
}
print(nested_dict)
print("-" * 30)