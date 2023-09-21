def write_to_file(f_name):
    with open(f_name, 'w') as file:
        while True:
            user_input = input("Enter a string (empty string to complete): ")
            if not user_input:
                break
            file.write(user_input + '\n')


filename = input("Enter a file name to record: ")

write_to_file(filename)
