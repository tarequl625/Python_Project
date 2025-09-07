# -------------------------------
# Decimal to Binary Conversion (Using Recursion)
# -------------------------------

# Take decimal input from user
number = int(input("Enter decimal number : "))

# Recursive function to convert decimal to binary
def decBin(n):
    if n > 1:
        decBin(n // 2)      # Recursive call for quotient
    print(n % 2, end="")    # Print remainder

# Call the recursive function
decBin(number)

# -------------------------------
# Example Run - 1:
# Input : 10
# Output: 1010
#
# Example Run - 2:
# Input : 25
# Output: 11001
# -------------------------------