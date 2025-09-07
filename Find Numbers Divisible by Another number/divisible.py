# -------------------------------
# Type - 1 (Find divisors using for loop)
# -------------------------------

# Take number input from user
number = int(input("Enter a number : "))

# Find divisors using for loop
for i in range(1, number + 1):
    if number % i == 0:
        print(f"Divisor of {number}: {i}")

# -------------------------------
# Example Run - 1:
# Input : 12
# Output:
# Divisor of 12: 1
# Divisor of 12: 2
# Divisor of 12: 3
# Divisor of 12: 4
# Divisor of 12: 6
# Divisor of 12: 12
# -------------------------------


# -------------------------------
# Type - 2 (Find divisors using lambda and filter)
# -------------------------------

# Using lambda and filter to find divisors
result = list(filter(lambda x: number % x == 0, range(1, number + 1)))

# Print all divisors
print(f"Divisors of {number} are: {result}")

# -------------------------------
# Example Run - 1:
# Input : 18
# Output: Divisors of 18 are: [1, 2, 3, 6, 9, 18]
# -------------------------------