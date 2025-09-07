# -------------------------------
# Prime Number Check (Basic Method)
# -------------------------------

# Take input from user
number = int(input("Enter a number : "))

# Special case for 1
if number == 1:
    print(f"{number} is not a prime number")

# Check for numbers greater than 1
elif number > 0:
    for i in range(2, number):       # loop from 2 to number-1
        if number % i == 0:          # if divisible, not prime
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")

# -------------------------------
# Example Run - 1:
# Input : 7
# Output: 7 is a prime number
#
# Example Run - 2:
# Input : 10
# Output: 10 is not a prime number
#
# Example Run - 3:
# Input : 1
# Output: 1 is not a prime number
# -------------------------------