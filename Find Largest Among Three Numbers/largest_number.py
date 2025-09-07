# -------------------------------
# Find the Largest Number Among Three Numbers
# -------------------------------

# Take three numbers input from user
number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))
number3 = int(input("Enter third number : "))

# Compare numbers to find the largest
if number1 > number2 and number1 > number3:
    print(f"{number1} is the largest number")
elif number2 > number1 and number2 > number3:
    print(f"{number2} is the largest number")
else:
    print(f"{number3} is the largest number")

# -------------------------------
# Example Run - 1:
# Input : 10, 25, 15
# Output: 25 is the largest number
#
# Example Run - 2:
# Input : 7, 3, 9
# Output: 9 is the largest number
# -------------------------------