# -------------------------------
# Type - 1 (Exponent 0.5)
# -------------------------------
number = 64
square = number ** 0.5
print("The square root of the given number is:", square)
# Output: The square root of the given number is: 8.0

# -------------------------------
# Type - 2 (Exponent 1/2)
# -------------------------------
number = 64
square = number ** (1/2)
print("The square root of the given number is:", square)
# Output: The square root of the given number is: 8.0

# -------------------------------
# Type - 3 (math.sqrt for real numbers)
# -------------------------------
import math
number = float(input("Enter a number to find the square root: "))  # Example input: 25
square = math.sqrt(number)
print("The square root of the given number is: %.3f" % square)
# Output: The square root of the given number is: 5.000

# -------------------------------
# Type - 4 (cmath.sqrt for real & complex numbers)
# -------------------------------
import cmath
number = int(input("Enter a number to find the square root: "))   # Example input: -25
square = cmath.sqrt(number)
print("The square root of the given number is: {0:.2}".format(square))
# Output (if input = -25): The square root of the given number is: 5j
# Output (if input = 25): The square root of the given number is: (5+0j)