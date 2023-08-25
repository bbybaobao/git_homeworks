number = input("Enter a number from 3 to 9: ")

if number.isdigit():
    number = int(number)
    if 3 <= number <= 9:
        for i in range(1, number + 1):
            row = ''.join(str(j) for j in range(1, i + 1))
            print(row)
    else:
        print("Number not in the range 3 to 9.")
else:
    print("Error: Please enter a number.")
