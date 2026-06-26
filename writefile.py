
try:
    # Open file in write mode
    with open('report.txt', 'w') as file:
        file.write('I love Python Programming\n')
        file.write('I am becoming a data Scientist')
    
    print("✅ File created successfully!")
    
    # Read and display the file content
    with open('report.txt', 'r') as file:
        print("\n📖 File content:")
        print(file.read())
        
except Exception as e:
    print(f"Error: {e}")