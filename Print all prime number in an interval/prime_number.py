# -------------------------------
# Prime Numbers in a Range
# -------------------------------

# Take start and end numbers from user
startnumber = int(input("Enter starting number : "))
endnumber = int(input("Enter ending number : "))

# Loop through each number in the range
for i in range(startnumber, endnumber + 1):
    if i > 1:  # 0 and 1 are not prime
        # Check if i is divisible by any number from 2 to i-1
        for j in range(2, i):
            if i % j == 0:
                print(f"{i} is not a prime number")
                break
        else:
            # If no divisor found, number is prime
            print(f"{i} is a prime number")

# -------------------------------
# Example Run - 1:
# Input : Start = 10, End = 15
# Output:
# 10 is not a prime number
# 11 is a prime number
# 12 is not a prime number
# 13 is a prime number
# 14 is not a prime number
# 15 is not a prime number
# -------------------------------