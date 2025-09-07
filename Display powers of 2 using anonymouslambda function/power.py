# -------------------------------
# Generate Powers of 2 using Lambda and Map
# -------------------------------

# Take number of terms input from user
terms = int(input("Enter number of terms : "))

# Generate powers of 2 from 0 to terms
result = list(map(lambda x: 2**x, range(terms + 1)))

# Print the powers of 2
for i in range(terms + 1):
    print(f"2**{i} = {result[i]}")

# -------------------------------
# Example Run - 1:
# Input : 5
# Output:
# 2**0 = 1
# 2**1 = 2
# 2**2 = 4
# 2**3 = 8
# 2**4 = 16
# 2**5 = 32
#
# Example Run - 2:
# Input : 3
# Output:
# 2**0 = 1
# 2**1 = 2
# 2**2 = 4
# 2**3 = 8
# -------------------------------