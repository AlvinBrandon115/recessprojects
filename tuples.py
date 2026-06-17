# Question 1: Output your favorite phone brand
print("Question 1:")
x = ("samsung", "iphone", "tecno", "redmi")
print(x[1])  # Assuming iphone is favorite
print("-" * 30)

# Question 2: Negative indexing to print 2nd last item
print("Question 2:")
x = ("samsung", "iphone", "tecno", "redmi")
print(x[-2])
print("-" * 30)

# Question 3: Update "iphone" to "itel"
print("Question 3:")
x = ("samsung", "iphone", "tecno", "redmi")
x_list = list(x)
x_list[1] = "itel"
x = tuple(x_list)
print(x)
print("-" * 30)

# Question 4: Add "Huawei" to tuple
print("Question 4:")
x = ("samsung", "iphone", "tecno", "redmi")
x_list = list(x)
x_list.append("Huawei")
x = tuple(x_list)
print(x)
print("-" * 30)

# Question 5: Loop through the tuple
print("Question 5:")
x = ("samsung", "iphone", "tecno", "redmi")
for brand in x:
    print(brand)
print("-" * 30)

# Question 6: Remove/delete the first item
print("Question 6:")
x = ("samsung", "iphone", "tecno", "redmi")
x_list = list(x)
x_list.pop(0)
x = tuple(x_list)
print(x)
print("-" * 30)

# Question 7: Create a tuple of cities in Uganda using tuple() constructor
print("Question 7:")
uganda_cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu"])
print(uganda_cities)
print("-" * 30)

# Question 8: Unpack your tuple
print("Question 8:")
uganda_cities = ("Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu")
city1, city2, city3, city4, city5 = uganda_cities
print(city1, city2, city3, city4, city5)
print("-" * 30)

# Question 9: Range of indexes to print 2nd, 3rd, 4th cities
print("Question 9:")
uganda_cities = ("Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu")
print(uganda_cities[1:4])
print("-" * 30)

# Question 10: Join two tuples
print("Question 10:")
first_names_tuple = ("Alvin", "John", "Mary")
second_names_tuple = ("Brandon", "Doe", "Jane")
full_names_tuple = first_names_tuple + second_names_tuple
print(full_names_tuple)
print("-" * 30)

# Question 11: Create a tuple of colors and multiply by 3
print("Question 11:")
colors = ("red", "blue", "green")
colors_multiplied = colors * 3
print(colors_multiplied)
print("-" * 30)

# Question 12: Count occurrences of 8 in the tuple
print("Question 12:")
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print(count_8)
print("-" * 30)
