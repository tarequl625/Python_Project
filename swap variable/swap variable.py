# -------------------------------
# Type - 1 (Using a temporary variable - static values)
# -------------------------------
firstVariable = 10
secondVariable = 20
temporaryVariable = secondVariable
secondVariable = firstVariable
firstVariable = temporaryVariable

print("first variable is", firstVariable)   # Output: 20
print("second variable is", secondVariable) # Output: 10

# -------------------------------
# Type - 2 (Using a temporary variable - user input)
# -------------------------------
firstVariable = int(input("Enter first value: "))   # Example input: 5
secondVariable = int(input("Enter second value: ")) # Example input: 8
temporaryVariable = secondVariable
secondVariable = firstVariable
firstVariable = temporaryVariable

print("first variable is", firstVariable)   # Output: 8
print("second variable is", secondVariable) # Output: 5

# -------------------------------
# Type - 3 (Tuple unpacking / Pythonic way)
# -------------------------------
firstVariable = int(input("Enter first value: "))   # Example input: 100
secondVariable = int(input("Enter second value: ")) # Example input: 200
secondVariable, firstVariable = firstVariable, secondVariable

print("first variable is", firstVariable)   # Output: 200
print("second variable is", secondVariable) # Output: 100

# -------------------------------
# Type - 4 (Multiple input with split)
# -------------------------------
firstVariable, secondVariable, *other = input("Enter first and second value (space separated): ").split()
secondVariable, firstVariable = firstVariable, secondVariable

print("first variable is", firstVariable)   # If input: 10 20 → Output: 20
print("second variable is", secondVariable) # If input: 10 20 → Output: 10