# -------------------------------
# Octal to Hexadecimal Conversion
# -------------------------------

# Take octal number input as string
octal = input("Enter an octal number : ")

# Convert octal (base 8) to hexadecimal
hexa = hex(int(octal, 8)).replace('0x', '').upper()  # Remove '0x' and capitalize

# Print result
print(f"{octal} Octal = {hexa} Hexadecimal")

# -------------------------------
# Example Run - 1:
# Input : 12
# Output: 12 Octal = A Hexadecimal
#
# Example Run - 2:
# Input : 77
# Output: 77 Octal = 3F Hexadecimal
# -------------------------------