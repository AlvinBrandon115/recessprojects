"""
File Handling - CSV Reader
Author: Ssebugwawo Alvin Brandon
"""

try:
    # Read the CSV file (use a raw string for Windows path)
    with open(r"C:\Users\Alvin Brandon\OneDrive\Documents\students.csv", 'r') as file:
        # Read all lines
        lines = file.readlines()
        
        print("=" * 80)
        print("STUDENT DATA FROM students.csv")
        print("=" * 80)
        print(f"👤 Read by: Ssebugwawo Alvin Brandon")
        print("=" * 80)
        
        # Display each line as a list
        for line in lines:
            # Remove newline and split by comma
            data = line.strip().split(',')
            print(data)
            
        print("=" * 80)
        print(f"✅ Total records read: {len(lines)}")
        print("=" * 80)
        
except FileNotFoundError:
    print("❌ File 'students.csv' not found!")
except Exception as e:
    print(f"❌ An error occurred: {e}")
