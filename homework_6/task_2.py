import random

user_number = int(input("Загадайте число от 0 до 100: "))

steps = 0

min_number = 0
max_number = 100

while True:
    guessed_number = random.randint(min_number, max_number)
    response = input(f"Это число {guessed_number}? (да/больше/меньше): ")
    steps += 1

    if response.lower() == "да":
        print(f"Программа угадала ваше число {guessed_number} за {steps} шагов.")
        break
    elif response.lower() == "больше":
        min_number = guessed_number + 1
    elif response.lower() == "меньше":
        max_number = guessed_number - 1
    else:
        print("Пожалуйста, введите 'да', 'больше' или 'меньше'.")

print("Игра завершена.")
