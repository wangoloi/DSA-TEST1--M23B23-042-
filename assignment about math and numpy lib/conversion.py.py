import math


# convert degrees to radians using the math.radians function
def deg_to_rad(deg):
    # Use the math.radians function to convert degrees to radians
    rad = math.radians(deg)
    return rad


# Ask the user to enter a value in degrees
deg = float(input("Enter a value in degrees: "))

# Call the function and print the result
rad = deg_to_rad(deg)
print(f"{deg} degrees is equal to {rad} radians.")
