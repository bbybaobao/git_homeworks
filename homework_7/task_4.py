numbers = input("Enter a list of integers separated by spaces: ")
numbers = [int(x) for x in numbers.split()]

min_index = max_index = 0
for i in range(1, len(numbers)):
    if numbers[i] < numbers[min_index]:
        min_index = i
    if numbers[i] > numbers[max_index]:
        max_index = i

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

result = ""
for num in numbers:
    result += str(num) + " "

print(result)
