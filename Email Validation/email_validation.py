import re
email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
def validation_email(email):
    if email_pattern.match(email):
        return True
    return False
print(validation_email("tarequl625@gmail.com"))