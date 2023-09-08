numbers = list(range(10, 251))

filtered_numbers = [num for num in numbers if num % 20 != 0]

# для лучшей читаемости!!
for i in range(0, len(filtered_numbers), 30):
    print(*filtered_numbers[i:i+30])