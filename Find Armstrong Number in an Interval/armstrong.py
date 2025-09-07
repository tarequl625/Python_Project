# -------------------------------
# Armstrong Number Check in a Range
# -------------------------------

# Take starting and ending numbers from user
startnumber = int(input("Enter starting number : "))
endnumber = int(input("Enter ending number : "))

# Loop through each number in the range
for i in range(startnumber, endnumber + 1):
    sum_of_powers = 0
    temp = i
    num_digits = len(str(i))  # Number of digits in current number

    # Calculate sum of digits raised to the power of num_digits
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** num_digits
        temp = temp // 10

    # Check if sum equals the original number
    if sum_of_powers == i:
        print(f"{i} is an Armstrong Number")
    else:
        print(f"{i} is not an Armstrong Number")

# -------------------------------
# Example Run - 1:
# Input : Start = 100, End = 150
# Output:
# 100 is not an Armstrong Number
# 101 is not an Armstrong Number
# ...
# 153 is an Armstrong Number
# -------------------------------