import math


# Define function to find LCM of two numbers
def lcm(a, b):
    return (a * b) // math.gcd(a, b)


# Define function to find LCM of a list of numbers
def lcm_list(lst):
    result = lst[0]
    for i in range(1, len(lst)):
        result = lcm(result, lst[i])
    return result


# the function to find factors of a number
def factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


# getting the values from the user
n = int(input("Enter n: "))

# Create list of numbers from 1 to n
numbers = list(range(1, n + 1))

# Find LCM of list
lcm_value = lcm_list(numbers)

# Find factors of LCM
lcm_factors = factors(lcm_value)

# Print list, LCM, and factors
print(f"The list of numbers from 1 to {n} is {numbers}")
print(f"The smallest multiple of these numbers is {lcm_value}")
print(f"The factors of {lcm_value} are {lcm_factors}")
