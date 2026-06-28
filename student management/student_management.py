import csv
import json
import logging
import os

# Configure logging so actions and errors go to the project folder.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "student_system.log")
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s %(levelname)s:%(message)s")

CSV_FILE = os.path.join(BASE_DIR, "students.csv")
JSON_FILE = os.path.join(BASE_DIR, "students.json")


class StudentNotFoundError(Exception):
    """Raised when a student registration number cannot be found."""


def ensure():
    """Create the CSV/JSON files if they do not already exist."""
    try:
        if not os.path.exists(CSV_FILE):
            with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow(["reg_no", "name", "age"])
        if not os.path.exists(JSON_FILE):
            with open(JSON_FILE, "w", encoding="utf-8") as f:
                json.dump({}, f, indent=2)
    except Exception as e:
        logging.exception("Failed to initialize storage files: %s", e)


def load_json():
    """Load JSON student data, supporting both dict and older list formats."""
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return {}

    if isinstance(data, dict):
        return data

    if isinstance(data, list):
        mapping = {}
        try:
            with open(CSV_FILE, "r", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    name = row.get("name", "").strip().lower()
                    for item in data:
                        if isinstance(item, dict) and item.get("name", "").strip().lower() == name:
                            mapping[row.get("reg_no")] = item
                            break
        except Exception as e:
            logging.exception("Failed to migrate list-format JSON: %s", e)
        if mapping:
            save_json(mapping)
        return mapping
    return {}


def save_json(data):
    """Save JSON student data."""
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def validate_reg_no(value):
    if not value or not value.strip():
        raise ValueError("Registration number cannot be empty.")
    return value.strip()


def validate_age(value):
    if not value or not value.strip():
        raise ValueError("Age cannot be empty.")
    try:
        age = int(value)
    except ValueError as exc:
        raise ValueError("Age must be a whole number.") from exc
    if age < 1:
        raise ValueError("Age must be greater than zero.")
    return age


def add():
    """Add a new student to the CSV and JSON files."""
    try:
        reg_no = validate_reg_no(input("Reg No: "))
        name = input("Name: ").strip()
        age = validate_age(input("Age: "))
        address = input("Address: ").strip()
        contact = input("Contact: ").strip()
        program = input("Program: ").strip()

        if not name:
            raise ValueError("Name cannot be empty.")

        with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([reg_no, name, age])

        data = load_json()
        data[reg_no] = {
            "name": name,
            "age": age,
            "address": address,
            "contact": contact,
            "program": program,
            "reg_no": reg_no,
        }
        save_json(data)
        logging.info("Added %s", reg_no)
    except Exception as e:
        logging.exception("Add failed: %s", e)
        print(e)
    finally:
        print("Done.")


def view():
    """Show all student records from the CSV file."""
    try:
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            for row in csv.reader(f):
                print(row)
    except Exception as e:
        logging.exception("View failed: %s", e)
        print(e)
    finally:
        print("---")


def search():
    """Search for one student and print their combined CSV/JSON details."""
    try:
        reg_no = validate_reg_no(input("Reg No: "))
        found = False
        students = load_json()
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row["reg_no"].strip() == reg_no:
                    details = students.get(reg_no, {})
                    record = {**row, **details}
                    record["reg_no"] = reg_no
                    if "Age" in record and "age" in record:
                        record["age"] = record["Age"]
                        del record["Age"]
                    print(json.dumps(record, indent=2))
                    found = True
        if not found:
            raise StudentNotFoundError("Student not found")
        logging.info("Searched %s", reg_no)
    except Exception as e:
        logging.exception("Search failed: %s", e)
        print(e)


def update():
    """Update a student's CSV name and age, and synchronize the JSON record."""
    try:
        reg_no = validate_reg_no(input("Reg No: "))
        rows = []
        found = False
        for row in csv.DictReader(open(CSV_FILE, "r", encoding="utf-8")):
            if row["reg_no"] == reg_no:
                found = True
                row["name"] = input("New name: ").strip()
                row["age"] = validate_age(input("New age: "))
            rows.append(row)

        if not found:
            raise StudentNotFoundError("Student not found")

        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["reg_no", "name", "age"])
            writer.writeheader()
            writer.writerows(rows)

        data = load_json()
        if reg_no in data:
            data[reg_no]["name"] = rows[0]["name"] if False else next(row["name"] for row in rows if row["reg_no"] == reg_no)
            data[reg_no]["age"] = next(int(row["age"]) for row in rows if row["reg_no"] == reg_no)
        save_json(data)
        logging.info("Updated %s", reg_no)
    except Exception as e:
        logging.exception("Update failed: %s", e)
        print(e)


def delete():
    """Delete a student from the CSV and JSON files."""
    try:
        reg_no = validate_reg_no(input("Reg No: "))
        rows = []
        found = False
        for row in csv.DictReader(open(CSV_FILE, "r", encoding="utf-8")):
            if row["reg_no"] == reg_no:
                found = True
            else:
                rows.append(row)

        if not found:
            raise StudentNotFoundError("Student not found")

        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["reg_no", "name", "age"])
            writer.writeheader()
            writer.writerows(rows)

        data = load_json()
        data.pop(reg_no, None)
        save_json(data)
        logging.info("Deleted %s", reg_no)
    except Exception as e:
        logging.exception("Delete failed: %s", e)
        print(e)


ensure()

while True:
    print("1.Add 2.View 3.Search 4.Update 5.Delete 6.Exit")
    choice = input("Choice: ").strip()
    if choice == "1":
        add()
    elif choice == "2":
        view()
    elif choice == "3":
        search()
    elif choice == "4":
        update()
    elif choice == "5":
        delete()
    elif choice == "6":
        break
    else:
        print("Please enter a valid choice.")
