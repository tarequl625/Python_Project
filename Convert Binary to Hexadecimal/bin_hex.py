# -------------------------------
# Binary to Hexadecimal Conversion
# -------------------------------

# Take binary number input as string
binary = input("Enter a binary number : ")

# Convert binary (base 2) to hexadecimal
hexa = hex(int(binary, 2)).replace("0x", "").upper()

# Print result
print(f"{binary} Binary = {hexa} Hexadecimal")

# -------------------------------
# Example Run - 1:
# Input : 1010
# Output: 1010 Binary = A Hexadecimal
#
# Example Run - 2:
# Input : 11111111
# Output: 11111111 Binary = FF Hexadecimal
# -------------------------------