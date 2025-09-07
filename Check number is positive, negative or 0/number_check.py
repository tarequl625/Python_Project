# -------------------------------
# Type - 1 (Check if a number is Positive, Negative, or Zero using if-elif-else)
# -------------------------------

# Take input from user
number = int(input("Enter a number : "))

# Check conditions
if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is zero")

# -------------------------------
# Example Run - 1:
# Input : 15
# Output: Number is positive
#
# Example Run - 2:
# Input : -7
# Output: Number is negative
#
# Example Run - 3:
# Input : 0
# Output: Number is zero
# -------------------------------


# -------------------------------
# Type - 2 (Check using Nested Ternary Operator in One Line)
# -------------------------------

# Shorthand for if-elif-else
print("Number is positive") if number > 0 else print("Number is negative") if number < 0 else print("Number is zero")

# -------------------------------
# Example Run - 1:
# Input : 25
# Output: Number is positive
#
# Example Run - 2:
# Input : -10
# Output: Number is negative
#
# Example Run - 3:
# Input : 0
# Output: Number is zero
# -------------------------------