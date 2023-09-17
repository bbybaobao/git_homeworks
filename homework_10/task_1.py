import random

numbers = [random.randint(1, 10) for _ in range(20)]

most_common_number = max(set(numbers), key=numbers.count)

print("Generated list:", numbers)
print("The number that appears often:", most_common_number)
