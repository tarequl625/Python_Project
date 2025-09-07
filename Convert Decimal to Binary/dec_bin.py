# -------------------------------
# Decimal to Binary Conversion
# -------------------------------

# Take decimal input from user
decimal = int(input("Enter a decimal number : "))

# Convert decimal to binary
binary = bin(decimal).replace('0b', '')  # Remove the '0b' prefix

# Print result
print(f"{decimal} Decimal = {binary} Binary")

# -------------------------------
# Example Run - 1:
# Input : 10
# Output: 10 Decimal = 1010 Binary
#
# Example Run - 2:
# Input : 255
# Output: 255 Decimal = 11111111 Binary
# -------------------------------