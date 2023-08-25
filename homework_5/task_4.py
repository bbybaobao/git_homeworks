user_input = input("Enter a string (at least 15 characters): ")

if len(user_input) < 15:
    print("The string must be at least 15 characters.")
else:
    print(f"Third character: {user_input[2]}")
    print(f"Penultimate character: {user_input[-2]}")
    print(f"First five characters: {user_input[:5]}")
    print(f"A string without the last two characters: {user_input[:-2]}")
    print(f"Symbols with paired indices: {user_input[::2]}")
    print(f"Symbols with odd indices: {user_input[1::2]}")
    print(f"Symbols in reverse order: {user_input[::-1]}")
    print(f"Characters through one in reverse order: {user_input[::-2]}")
    print(f"Line length: {len(user_input)}")
