# -------------------------------
# Hexadecimal to Octal Conversion
# -------------------------------

# Take hexadecimal input from user
hexadecimal = input("Enter a hexadecimal number : ")

# Convert hexadecimal (base 16) to octal
octal = oct(int(hexadecimal, 16)).replace('0o', '')

# Print result
print(f"{hexadecimal} Hexadecimal = {octal} Octal")

# -------------------------------
# Example Run - 1:
# Input : A
# Output: A Hexadecimal = 12 Octal
#
# Example Run - 2:
# Input : 1F
# Output: 1F Hexadecimal = 37 Octal
# -------------------------------