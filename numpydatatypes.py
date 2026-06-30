import numpy as np

# Integer Array
int_arr = np.array([10, 20, 30], dtype=int)
print("Integer Array:")
print(int_arr)
print("Data Type:", int_arr.dtype)

# Float Array
float_arr = np.array([10.5, 20.8, 30.2], dtype=float)
print("\nFloat Array:")
print(float_arr)
print("Data Type:", float_arr.dtype)

# Boolean Array
bool_arr = np.array([True, False, True], dtype=bool)
print("\nBoolean Array:")
print(bool_arr)
print("Data Type:", bool_arr.dtype)

# String Array
str_arr = np.array(["Alice", "Bob", "Carol"], dtype=str)
print("\nString Array:")
print(str_arr)
print("Data Type:", str_arr.dtype)

# Complex Number Array
complex_arr = np.array([2+3j, 4+5j], dtype=complex)
print("\nComplex Number Array:")
print(complex_arr)
print("Data Type:", complex_arr.dtype)

# -------------------------------
# Data Type Conversion Examples
# -------------------------------

# Integer to Float
int_to_float = int_arr.astype(float)
print("\nInteger to Float:")
print(int_to_float)
print("Data Type:", int_to_float.dtype)

# Float to Integer
float_to_int = float_arr.astype(int)
print("\nFloat to Integer:")
print(float_to_int)
print("Data Type:", float_to_int.dtype)

# Integer to String
int_to_str = int_arr.astype(str)
print("\nInteger to String:")
print(int_to_str)
print("Data Type:", int_to_str.dtype)

# Boolean to Integer
bool_to_int = bool_arr.astype(int)
print("\nBoolean to Integer:")
print(bool_to_int)
print("Data Type:", bool_to_int.dtype)