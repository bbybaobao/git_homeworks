saved_password = "qwerty1234"
input_password = input("Enter password: ")

if input_password in saved_password:
    print("Right password.")
else:
    print("Wrong password. Try again.")
