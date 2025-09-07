# -------------------------------
# Email Validation using Regular Expressions
# -------------------------------

# Import the 're' module
import re

# Define the email pattern using regex
email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

# Function to validate email
def validation_email(email):
    if email_pattern.match(email):
        return True
    return False

# Test the function
print(validation_email("tarequl625@gmail.com"))  # Output: True

# -------------------------------
# Example Run - 1:
# Input : "test.user@example.com"
# Output: True
#
# Example Run - 2:
# Input : "invalid-email@"
# Output: False
# -------------------------------