# -------------------------------
# Sum of First N Natural Numbers (Using Recursion)
# -------------------------------

# Take number input from user
number = int(input("Enter a number : "))

# Recursive function to calculate sum
def sum_natural(n):
    if n <= 0:       # Base case
        return 0
    else:
        return n + sum_natural(n - 1)  # Recursive call

# Print the sum
print(f"Sum of first {number} natural numbers is {sum_natural(number)}")

# -------------------------------
# Example Run - 1:
# Input : 5
# Output: Sum of first 5 natural numbers is 15
#
# Example Run - 2:
# Input : 10
# Output: Sum of first 10 natural numbers is 55
# -------------------------------