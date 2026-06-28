#creating a JSON file
# import json

# student = {
#     "name": "Jeff",
#     "Age": "24",
#     "Course": "Python"
# }

# with open("student.json", "w") as file:
#     json.dump(student, file, indent=4)

# print("JSON file created successfully")

#reading a JSON file
# import json

# with open("student.json", "r") as file:
#     student = json.load(file)

# print(student)
# print("Name:", student["name"])
# print("Age:", student["Age"])
# print("Course:", student["Course"])

#writing multiple students to a JSON file
import json

students = [
    {
        "name": "Alvin",
        "Age": 22,
        "Course": "Computer Science"
    },
    {
        "name": "Sarah",
        "Age": 21,
        "Course": "Information Technology"
    },
    {
        "name": "Brian",
        "Age": 23,
        "Course": "Software Engineering"
    }
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Students saved successfully.")