# Question 1: Use set() constructor to create set of 3 favorite beverages
print("Question 1:")
beverages = set(["coffee", "tea", "juice"])
print(beverages)
print("-" * 30)

# Question 2: Add 2 more items to the beverages set
print("Question 2:")
beverages = set(["coffee", "tea", "juice"])
beverages.add("milk")
beverages.add("soda")
print(beverages)
print("-" * 30)

# Question 3: Check if "microwave" is present in the set
print("Question 3:")
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("True")
else:
    print("False")
print("-" * 30)

# Question 4: Remove "kettle" from the set
print("Question 4:")
mySet = {"oven", "kettle", "microwave", "refrigerator"}
mySet.remove("kettle")
print(mySet)
print("-" * 30)

# Question 5: Loop through the set
print("Question 5:")
mySet = {"oven", "kettle", "microwave", "refrigerator"}
for item in mySet:
    print(item)
print("-" * 30)

# Question 6: Add elements in list to set
print("Question 6:")
my_set = {"apple", "banana", "mango", "orange"}
my_list = ["grape", "kiwi"]
my_set.update(my_list)
print(my_set)
print("-" * 30)

# Question 7: Join two sets
print("Question 7:")
ages = {20, 22, 25}
first_names_set = {"Alvin", "John", "Mary"}
joined_set = ages.union(first_names_set)
print(joined_set)
print("-" * 30)