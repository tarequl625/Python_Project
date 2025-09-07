# -------------------------------
# Type - 1 (Leap Year Check - Simplified Condition)
# -------------------------------

# Take input from user
year = int(input("Enter year : "))

# Condition for leap year
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(f"{year} year is Leap Year")
else:
    print(f"{year} year is not Leap Year")

# -------------------------------
# Example Run - 1:
# Input : 2020
# Output: 2020 year is Leap Year
#
# Example Run - 2:
# Input : 1900
# Output: 1900 year is not Leap Year
# -------------------------------


# -------------------------------
# Type - 2 (Leap Year Check - Step by Step Conditions)
# -------------------------------

if (year % 400 == 0) and (year % 100 == 0):
    # If divisible by 400 → Leap Year
    print(f"{year} year is Leap Year")
elif (year % 4 == 0) and (year % 100 != 0):
    # If divisible by 4 but not by 100 → Leap Year
    print(f"{year} year is Leap Year")
else:
    # All other cases → Not Leap Year
    print(f"{year} year is not Leap Year")

# -------------------------------
# Example Run - 1:
# Input : 2000
# Output: 2000 year is Leap Year
#
# Example Run - 2:
# Input : 2100
# Output: 2100 year is not Leap Year
# -------------------------------