import numpy as np

# an array of numbers
arr = np.array([1 + 2j, 3.5, -2, 4j])

# Test element for complex numbers
print("Is complex:", np.iscomplex(arr))

# Test element for real numbers
print("Is real:", np.isreal(arr))

# Test if a given number is of a scalar type
print("Is scalar:", np.isscalar(5))
