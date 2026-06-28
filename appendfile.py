
try:
    # Open file in write mode
    with open('report.txt', 'w') as file:
        file.write('I love Python Programming\n')
        file.write('I am becoming a data Scientist')
    
    print("✅ File created successfully!")
    
    # Append more content
    with open('report.txt', 'a') as file:
        file.write('\nEvery data scientist must learn python')
    
    print("✅ Content appended successfully!")
    
    # Read and display the final file content
    with open('report.txt', 'r') as file:
        print("\n📖 Final File Content:")
        print("-" * 40)
        print(file.read())
        print("-" * 40)
        
except Exception as e:
    print(f"Error: {e}")