import cmath   # cmath is used because it supports complex numbers

# Input coefficients
a = int(input("Enter number of a: "))   # Example: 1
while a == 0:
    print("Value of a can't be 0")
    a = int(input("Enter another number of a: "))

b = int(input("Enter number of b: "))   # Example: -5
c = int(input("Enter number of c: "))   # Example: 6

# Discriminant
d = (b ** 2) - (4 * a * c)

# Roots formula: (-b ± √d) / 2a
root1 = (-b - cmath.sqrt(d)) / (2 * a)
root2 = (-b + cmath.sqrt(d)) / (2 * a)

# Print results with 2 decimal formatting
print("The roots are {0:.2f} and {1:.2f}".format(root1.real, root2.real)
      if d >= 0 else
      "The roots are {0} and {1}".format(root1, root2))