# -------------------------------
# Type - 1 (Factors using for loop and print)
# -------------------------------

# Take number input from user
number = int(input("Enter a number : "))

# Print factors one by one
for i in range(1, number + 1):
    if number % i == 0:
        print(f"Factor of number {number} is {i}")

# -------------------------------
# Example Run - 1:
# Input : 12
# Output:
# Factor of number 12 is 1
# Factor of number 12 is 2
# Factor of number 12 is 3
# Factor of number 12 is 4
# Factor of number 12 is 6
# Factor of number 12 is 12
# -------------------------------


# -------------------------------
# Type - 2 (Factors using list comprehension)
# -------------------------------

# Using list comprehension to get factors
factors = [str(i) for i in range(1, number + 1) if number % i == 0]

# Print all factors
print(f"Factors of number {number} are: {', '.join(factors)}")

# -------------------------------
# Example Run - 2:
# Input : 15
# Output: Factors of number 15 are: 1, 3, 5, 15
# -------------------------------


# -------------------------------
# Type - 3 (Factors using list and append)
# -------------------------------

# Initialize empty list
factor_list = []

# Append factors to the list
for i in range(1, number + 1):
    if number % i == 0:
        factor_list.append(str(i))

# Print all factors
print(f"Factors of number {number} are: {', '.join(factor_list)}")

# -------------------------------
# Example Run - 3:
# Input : 20
# Output: Factors of number 20 are: 1, 2, 4, 5, 10, 20
# -------------------------------