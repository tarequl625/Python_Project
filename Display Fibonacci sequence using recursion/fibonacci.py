# -------------------------------
# Fibonacci Series (Using Recursion)
# -------------------------------

# Take number of terms input from user
number = int(input("Enter the number of terms: "))

# Recursive function to generate Fibonacci numbers
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

# Print the Fibonacci series
for i in range(number):
    print(fibo(i), end=" ")

# -------------------------------
# Example Run - 1:
# Input : 5
# Output: 0 1 1 2 3
#
# Example Run - 2:
# Input : 8
# Output: 0 1 1 2 3 5 8 13
# -------------------------------