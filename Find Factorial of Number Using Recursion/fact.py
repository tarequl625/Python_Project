# -------------------------------
# Factorial using Recursion (Improved)
# -------------------------------

# Take number input from user
number = int(input("Enter a number : "))

# Recursive function to calculate factorial
def fact(n):
    if n == 0 or n == 1:   # Handle 0! and 1!
        return 1
    else:
        return n * fact(n - 1)

# Print factorial
print(f"{number}! = {fact(number)}")

# -------------------------------
# Example Run - 1:
# Input : 5
# Output: 5! = 120
#
# Example Run - 2:
# Input : 0
# Output: 0! = 1
# -------------------------------