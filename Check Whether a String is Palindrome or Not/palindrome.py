# -------------------------------
# Palindrome Check (String Method)
# -------------------------------

# Take input from user
word = input("Enter a word : ")

# Reverse the string using slicing
rev = word[::-1]

# Check if original and reversed strings are same
if word == rev:
    print(f"{word} is palindrome")
else:
    print(f"{word} is not palindrome")

# -------------------------------
# Example Run - 1:
# Input : madam
# Output: madam is palindrome
#
# Example Run - 2:
# Input : hello
# Output: hello is not palindrome
# -------------------------------