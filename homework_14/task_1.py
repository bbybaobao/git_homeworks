import re

def validate_password(password):
    if not password or any(char.isspace() for char in password):
        return None

    if not (any(char.isdigit() for char in password) and
            any(char.isalpha() for char in password) and
            any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>/?`~" for char in password) and
            len(password) >= 8):
        return None

    return password

def password_requirements(func):
    def wrapper():
        while True:
            print("Possible to the password: The password must be filled with 1 number, 1 letter, 1 special character and 8 characters..")
            password = func()
            if password:
                print("Received password:", password)
                return password

    return wrapper

@password_requirements
def get_password():
    password = input("Enter your password: ")
    return validate_password(password)

password = get_password()
