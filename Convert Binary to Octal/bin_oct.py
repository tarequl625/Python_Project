# -------------------------------
# Binary to Octal Conversion
# -------------------------------

# Take binary number input as string
binary = input("Enter a binary number : ")

# Convert binary (base 2) to octal
octal = oct(int(binary, 2)).replace('0o', '')

# Print result
print(f"{binary} Binary = {octal} Octal")

# -------------------------------
# Example Run - 1:
# Input : 1010
# Output: 1010 Binary = 12 Octal
#
# Example Run - 2:
# Input : 111111
# Output: 111111 Binary = 77 Octal
# -------------------------------