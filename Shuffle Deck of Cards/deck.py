# -------------------------------
# Remove Punctuation from a String
# -------------------------------

# Take a sentence input from user
sentence = input("Enter a sentence : ")

# Define punctuation characters to remove
punc = '''!()-{}[]:;'"\<>./?@#$%^&*_~'''

# Initialize empty string to store result
clean_sentence = ""

# Loop through each character and add to result if not punctuation
for i in sentence:
    if i not in punc:
        clean_sentence += i

# Print original and cleaned sentence
print(f"Original sentence: {sentence}")
print(f"Sentence without punctuation: {clean_sentence}")

# -------------------------------
# Example Run - 1:
# Input : Hello, World!
# Output:
# Original sentence: Hello, World!
# Sentence without punctuation: Hello World
#
# Example Run - 2:
# Input : Python@3.11 is awesome!
# Output:
# Original sentence: Python@3.11 is awesome!
# Sentence without punctuation: Python311 is awesome
# -------------------------------