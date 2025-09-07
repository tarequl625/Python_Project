# -------------------------------
# Email Validation without Regex
# -------------------------------

# Take email input from user
email = input("Enter your Email: ")

# Initialize flags
has_uppercase, has_space, has_invalid_char = 0, 0, 0

# Check minimum length
if len(email) >= 6:
    
    # First character must be a letter
    if email[0].isalpha():
        
        # Must contain exactly one '@'
        if ("@" in email) and (email.count("@") == 1):
            
            # Check if '.' is at -3 or -4 position
            if (email[-4] == ".") ^ (email[-3] == "."):
                
                # Loop through each character
                for char in email:
                    if char.isspace():
                        has_space = 1
                    elif char.isalpha() and char.isupper():
                        has_uppercase = 1
                    elif char.isdigit():
                        continue
                    elif char in ["_", ".", "@"]:
                        continue
                    else:
                        has_invalid_char = 1
                
                # Final validation
                if has_space == 1 or has_uppercase == 1 or has_invalid_char == 1:
                    print("Wrong Email")
                else:
                    print("You Entered a Correct Email")
            else:
                print("Wrong Email")
        else:
            print("Wrong Email")
    else:
        print("Wrong Email")
else:
    print("Wrong Email")

# -------------------------------
# Example Runs:
# Input : tarequl625@gmail.com
# Output: You Entered a Correct Email
#
# Input : Test@Example
# Output: Wrong Email
# -------------------------------