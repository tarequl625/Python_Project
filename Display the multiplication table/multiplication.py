# -------------------------------
# Type - 1 (Multiplication Table using for loop)
# -------------------------------

# Take number input from user
number = int(input("Enter a number : "))

# Print multiplication table using for loop
for i in range(1, 11):
    prod = i * number
    print(f"{i} x {number} = {prod}")

# -------------------------------
# Example Run - 1:
# Input : 5
# Output:
# 1 x 5 = 5
# 2 x 5 = 10
# 3 x 5 = 15
# ...
# 10 x 5 = 50
# -------------------------------


# -------------------------------
# Type - 2 (Multiplication Table using while loop)
# -------------------------------

# Initialize counter
i = 1

# Loop until 10
while i <= 10:
    print(f"{i} x {number} = {i * number}")
    i += 1

# -------------------------------
# Example Run - 1:
# Input : 7
# Output:
# 1 x 7 = 7
# 2 x 7 = 14
# ...
# 10 x 7 = 70
# -------------------------------