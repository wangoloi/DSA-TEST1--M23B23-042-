import math

# Getting base and height from user
base = input("Enter the base of the parallelogram: ")
height = input("Enter the height of the parallelogram: ")

# Convert strings to floats
base = float(base)
height = float(height)

# Calculate area
area = base * height

# Print area
print(f"The area of the parallelogram is {area:.1f} square units.")
