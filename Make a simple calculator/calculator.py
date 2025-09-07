# -------------------------------
# Simple Calculator Program
# -------------------------------

# Take two numbers input from user
number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))

# Display operation choices
print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")

# Take user choice
choice = int(input("Enter your choice (1-4): "))

# Perform operation based on choice
if choice == 1:
    print(f"The addition of {number1} and {number2} is {number1 + number2}")
elif choice == 2:
    print(f"The subtraction of {number1} and {number2} is {number1 - number2}")
elif choice == 3:
    print(f"The multiplication of {number1} and {number2} is {number1 * number2}")
elif choice == 4:
    # Handle division by zero
    if number2 != 0:
        print(f"The division of {number1} by {number2} is {number1 / number2}")
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid Choice! Please select 1-4")

# -------------------------------
# Example Run - 1:
# Input : 10, 5, Choice = 1
# Output: The addition of 10 and 5 is 15
#
# Example Run - 2:
# Input : 8, 2, Choice = 4
# Output: The division of 8 by 2 is 4.0
# -------------------------------