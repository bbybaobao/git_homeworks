rows = int(input("Enter the number of lines: "))

for i in range(rows + 1):
    spaces = ' ' * (rows - i)
    numbers = '1' + '0' * i
    print(f"{i:2}{spaces} {numbers}")
