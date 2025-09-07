# -------------------------------
# Remove Punctuation from a Sentence
# -------------------------------

# Take sentence input from user
sentence = input("Enter a sentence : ")

# Define punctuation characters
punc = '''!()-{}[]:;'"\<>./?@#$%^&*_~'''

# Initialize empty string to store result
clean_sentence = ""

# Loop through each character and exclude punctuation
for i in sentence:
    if i not in punc:
        clean_sentence += i

# Print original and cleaned sentence
print(f"Original sentence: {sentence}")
print(f"Sentence without punctuation: {clean_sentence}")

# -------------------------------
# Example Run - 1:
# Input : Hello, world! How are you?
# Output:
# Original sentence: Hello, world! How are you?
# Sentence without punctuation: Hello world How are you
# -------------------------------