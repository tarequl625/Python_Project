# -------------------------------
# Decimal to Octal Conversion
# -------------------------------

# Take decimal input from user
decimal = int(input("Enter a decimal number : "))

# Convert decimal to octal
octal = oct(decimal).replace('0o', '')  # Remove '0o' prefix

# Print result
print(f"{decimal} Decimal = {octal} Octal")

# -------------------------------
# Example Run - 1:
# Input : 10
# Output: 10 Decimal = 12 Octal
#
# Example Run - 2:
# Input : 64
# Output: 64 Decimal = 100 Octal
# -------------------------------