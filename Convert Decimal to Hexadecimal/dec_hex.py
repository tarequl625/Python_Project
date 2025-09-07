# -------------------------------
# Decimal to Hexadecimal Conversion
# -------------------------------

# Take decimal input from user
decimal = int(input("Enter a decimal number : "))

# Convert decimal to hexadecimal
hexa = hex(decimal).replace('0x', '').upper()  # Remove '0x' prefix and capitalize letters

# Print result
print(f"{decimal} Decimal = {hexa} Hexadecimal")

# -------------------------------
# Example Run - 1:
# Input : 255
# Output: 255 Decimal = FF Hexadecimal
#
# Example Run - 2:
# Input : 100
# Output: 100 Decimal = 64 Hexadecimal
# -------------------------------