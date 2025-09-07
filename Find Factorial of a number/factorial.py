# -------------------------------
# Type - 1 (Factorial using for loop)
# -------------------------------

# Take number input from user
number = int(input("Enter a number : "))
fact = 1

# Factorial for negative numbers does not exist
if number < 0:
    print("Factorial of negative number does not exist")

# Factorial of 0 is 1
elif number == 0:
    print(f"{number}! = 1")

# Factorial for positive numbers
else:
    for i in range(1, number + 1):
        fact = fact * i
    print(f"{number}! = {fact}")

# -------------------------------
# Type - 2 (Factorial using recursion)
# -------------------------------

# Recursive function to calculate factorial
def fact_recursive(n):
    if n == 0:
        return 1
    else:
        return n * fact_recursive(n - 1)

# Print factorial using recursion
print(f"{number}! = {fact_recursive(number)}")

# -------------------------------
# Example Run - 1:
# Input : 5
# Output: 5! = 120
#
# Example Run - 2:
# Input : 0
# Output: 0! = 1
# -------------------------------