string = input("Введите строку: ")
char = input("Введите символ для поиска: ")

positions = []

index = 0

while True:
    index = string.find(char, index)

    if index == -1:
        break
    positions.append(index)
    index += 1

if positions:
    print(f"Символ '{char}' найден на позициях: {positions}")
else:
    print(f"Символ '{char}' не найден в строке.")
