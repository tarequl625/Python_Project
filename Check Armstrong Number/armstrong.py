# -------------------------------
# Type - 1 (Armstrong Number Check - User Input)
# -------------------------------

# Take input from user
number = int(input("Enter a number : "))

# Initialize variables
sum = 0
temp = number

# Loop to extract digits and calculate cube of each digit
while temp > 0:
    digit = temp % 10         # Get last digit
    cube = digit ** 3         # Cube of the digit
    sum = sum + cube          # Add cube to sum
    temp = temp // 10         # Remove last digit

# Check Armstrong condition
if sum == number:
    print(f"{number} is Armstrong Number")
else:
    print(f"{number} is not Armstrong Number")

# -------------------------------
# Example Run - 1:
# Input : 153
# Output: 153 is Armstrong Number
#
# Example Run - 2:
# Input : 125
# Output: 125 is not Armstrong Number
# -------------------------------