# Question 1: Create a list with 5 items and output the 2nd item
print("Question 1:")
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(names[1])
print("-" * 30)

# Question 2: Change the value of the first item to a new value
print("Question 2:")
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
names[0] = "Zara"
print(names)
print("-" * 30)

# Question 3: Add a sixth item to the list
print("Question 3:")
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
names.append("Frank")
print(names)
print("-" * 30)

# Question 4: Add "Bathel" as the 3rd item
print("Question 4:")
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
names.insert(2, "Bathel")
print(names)
print("-" * 30)

# Question 5: Remove the 4th item
print("Question 5:")
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
names.pop(3)
print(names)
print("-" * 30)

# Question 6: Use negative indexing to print the last item
print("Question 6:")
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(names[-1])
print("-" * 30)

# Question 7: Create a new list with 7 items and print 3rd, 4th, 5th items
print("Question 7:")
new_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(new_list[2:5])
print("-" * 30)

# Question 8: List of countries and make a copy
print("Question 8:")
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda", "DR Congo"]
countries_copy = countries.copy()
print(countries_copy)
print("-" * 30)

# Question 9: Loop through the list of countries
print("Question 9:")
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda", "DR Congo"]
for country in countries:
    print(country)
print("-" * 30)

# Question 10: List of animal names, sort ascending and descending
print("Question 10:")
animals = ["lion", "elephant", "zebra", "giraffe", "hippo", "cheetah"]
animals.sort()
print(animals)
animals.sort(reverse=True)
print(animals)
print("-" * 30)

# Question 11: Output only animal names with the letter 'a'
print("Question 11:")
animals = ["lion", "elephant", "zebra", "giraffe", "hippo", "cheetah"]
for animal in animals:
    if 'a' in animal:
        print(animal)
print("-" * 30)

# Question 12: Join two lists
print("Question 12:")
first_names = ["Alvin", "John", "Mary"]
second_names = ["Brandon", "Doe", "Jane"]
full_names = first_names + second_names
print(full_names)
print("-" * 30)