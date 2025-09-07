# -------------------------------
# Type - 1 (Find HCF using iterative method)
# -------------------------------

# Take two numbers input from user
number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))

# Function to calculate HCF
def calHCF(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf

# Print HCF
print(f"HCF of {number1} and {number2} is: {calHCF(number1, number2)}")

# -------------------------------
# Type - 2 (Find all common factors)
# -------------------------------

# Function to find all common factors
def findHCF(x, y):
    smaller = min(x, y)
    common_factors = []
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            common_factors.append(str(i))
    return common_factors

# Print all common factors
print(f"Common factors of {number1} and {number2} are: {', '.join(findHCF(number1, number2))}")

# -------------------------------
# Example Run - 1:
# Input : number1 = 12, number2 = 18
# Output:
# HCF of 12 and 18 is: 6
# Common factors of 12 and 18 are: 1, 2, 3, 6
#
# Example Run - 2:
# Input : number1 = 20, number2 = 30
# Output:
# HCF of 20 and 30 is: 10
# Common factors of 20 and 30 are: 1, 2, 5, 10
# -------------------------------