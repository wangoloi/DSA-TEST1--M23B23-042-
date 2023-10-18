import numpy as np

# Create an array with values 1, 7, 13, 105
arr = np.array([1, 7, 13, 105], dtype=np.int32)

# Get number of elements in array
n = arr.size

# Get size of each element in bytes
b = arr.itemsize

# Get total memory size in bytes
m = n * b

# Print array and memory size
print(f"The array is {arr}")
print(f"The memory size is {m} bytes")
