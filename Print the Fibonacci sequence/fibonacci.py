# -------------------------------
# Fibonacci Series (Iterative Method)
# -------------------------------

# Initialize first two terms
firstNumber = 1
secondNumber = 1

# Print first two terms
print(firstNumber, end=" ")
print(secondNumber, end=" ")

# Print next 10 terms
for i in range(10):
    sum = firstNumber + secondNumber
    print(sum, end=" ")
    # Update values for next iteration
    firstNumber = secondNumber
    secondNumber = sum

# -------------------------------
# Example Output:
# 1 1 2 3 5 8 13 21 34 55 89 144
# -------------------------------