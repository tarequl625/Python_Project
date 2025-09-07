# -------------------------------
# Random Number Examples
# -------------------------------

import random

# Generate a random float number between 0.0 and 1.0
print("Random float between 0 and 1:", random.random())

# Generate a random integer between 0 and 100 (inclusive)
print("Random integer between 0 and 100:", random.randint(0, 100))

# Generate a random integer from 0 to 99 (range exclusive of 100)
print("Random number from range 0 to 100:", random.randrange(0, 100))

# -------------------------------
# Example Output (will vary each run):
# Random float between 0 and 1: 0.345678
# Random integer between 0 and 100: 56
# Random number from range 0 to 100: 23
# -------------------------------