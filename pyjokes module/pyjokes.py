# -------------------------------
# Random Programming Jokes Script
# -------------------------------

# Import the pyjokes library which contains a collection of programmer jokes
import pyjokes

# ------------------------------------
# Single Random Programming Joke
# ------------------------------------

# Get a single random programming joke
joke = pyjokes.get_joke(language='en', category='neutral')

# Print the single joke to the console
print("Single Joke:\n", joke)

# ------------------------------------
# Multiple Programming Jokes
# ------------------------------------

# Get a list of programming jokes (default is English and 'neutral' category)
jokes = pyjokes.get_jokes()

# Print a divider
print("\nMultiple Jokes:")

# Loop through the first 3 jokes and print them
for i in jokes[:3]:
    print("-", i)