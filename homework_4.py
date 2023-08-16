"""Task 1"""

# numbers = input("Enter numbers: ")
#
# duplicate = False
# for char in numbers:
#     if char.isdigit() and numbers.count(char) >= 2:
#         duplicate = True
#         print(f"{numbers} Yes")
#         break
#
# if not duplicate:
#     print(f"{numbers} No")

"""Task 2"""

# N = int(input("Enter natural number N: "))
# for i in range(1, N+1):
#     square = i * i
#     if str(square).endswith(str(i)):
#         print(f"{i}*{i}={square}")
# # str(square).endswith(str(i)) -- проверяет,
# # заканчивается ли число той же цифрой

"""Task 3"""

# numbers = []
# total_sum = even_count = odd_count = 0
#
# while True:
#     num = int(input("Enter numbers (to complete enter 0): "))
#     if num == 0:
#         break
#     numbers.append(num)
#
# for num in numbers:
#     total_sum += num
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
#
# if numbers:
#     average = total_sum / len(numbers)
#     print(f"Total sum: {total_sum}")
#     print(f"Average: {average}")
#     print(f"Max: {max(numbers)}")
#     print(f"Min: {min(numbers)}")
#     print(f"Even: {even_count}")
#     print(f"Odd: {odd_count}")
# else:
#     print("You enter 0.")
