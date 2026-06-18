a, b = 0, 1
fibonacci_list = []

for i in range(10):
    fibonacci_list.append(a)
    a, b = b, a + b

print(f"  First 10 Fibonacci numbers: {fibonacci_list}")
