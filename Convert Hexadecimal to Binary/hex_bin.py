# -------------------------------
# Hexadecimal to Binary Conversion
# -------------------------------

# Take hexadecimal input from user
hexadecimal = input("Enter a hexadecimal number : ")

# Convert hexadecimal (base 16) to binary
binary = bin(int(hexadecimal, 16)).replace('0b', '')

# Print result
print(f"{hexadecimal} Hexadecimal = {binary} Binary")

# -------------------------------
# Example Run - 1:
# Input : A
# Output: A Hexadecimal = 1010 Binary
#
# Example Run - 2:
# Input : 1F
# Output: 1F Hexadecimal = 11111 Binary
# -------------------------------