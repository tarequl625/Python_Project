# -------------------------------
# Octal to Binary Conversion
# -------------------------------

# Take octal number input as string
octal = input("Enter an octal number : ")

# Convert octal (base 8) to binary
binary = bin(int(octal, 8)).replace('0b', '')

# Print result
print(f"{octal} Octal = {binary} Binary")

# -------------------------------
# Example Run - 1:
# Input : 12
# Output: 12 Octal = 1010 Binary
#
# Example Run - 2:
# Input : 77
# Output: 77 Octal = 111111 Binary
# -------------------------------