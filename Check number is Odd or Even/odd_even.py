# -------------------------------
# Type - 1 (Even-Odd Check using if-else)
# -------------------------------

# Take input from user
number = int(input("Enter a number : "))

# Check if number is divisible by 2
if number % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

# -------------------------------
# Example Run - 1:
# Input : 12
# Output: Number is Even
#
# Example Run - 2:
# Input : 7
# Output: Number is Odd
# -------------------------------


# -------------------------------
# Type - 2 (Even-Odd Check using Ternary Operator)
# -------------------------------

# One-line shorthand for if-else
print("Number is Even") if number % 2 == 0 else print("Number is Odd")

# -------------------------------
# Example Run - 1:
# Input : 20
# Output: Number is Even
#
# Example Run - 2:
# Input : 15
# Output: Number is Odd
# -------------------------------