# -------------------------------
# Sum of Natural Numbers from 0 to N
# -------------------------------

# Take the end range from user
endNumber = int(input("Enter end range of natural number : "))

# Initialize sum
sum = 0

# Loop through 0 to endNumber
for i in range(endNumber + 1):
    sum += i

# Print the sum
print(f"Sum of natural numbers from 0 to {endNumber} is {sum}")

# -------------------------------
# Example Run - 1:
# Input : 5
# Output: Sum of natural numbers from 0 to 5 is 15
#
# Example Run - 2:
# Input : 10
# Output: Sum of natural numbers from 0 to 10 is 55
# -------------------------------