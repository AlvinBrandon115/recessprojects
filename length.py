
fruits = ['Cherry', 'Banana', 'Date', 'Apple', 'Mango', 'DragonFruit']

print("=" * 50)
print("SORTING WORDS BY LENGTH USING LAMBDA")
print("=" * 50)

# Original list
print(f"\n📋 Original list:")
print(f"  {fruits}")

# Sort by length (ascending - shortest to longest)
sorted_by_length = sorted(fruits, key=lambda x: len(x))
print(f"\n📊 Sorted by length (shortest to longest):")
print(f"  {sorted_by_length}")