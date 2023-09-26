import random


def generate_matrix(m):
    return [[random.randint(1, 50) for _ in range(m)] for _ in range(m)]


def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(f'{element:2}', end=' ')
        print()


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def column_sums(matrix):
    return [sum(col) for col in zip(*matrix)]


def sort_columns(matrix):
    column_sums_list = column_sums(matrix)
    bubble_sort(column_sums_list)
    sorted_matrix = [list(col) for _, col in sorted(zip(column_sums_list, zip(*matrix)))]
    return sorted_matrix


def sort_odd_even(matrix):
    for i in range(len(matrix)):
        if i % 2 == 0:
            bubble_sort(matrix[i])
        else:
            bubble_sort(matrix[i])
            matrix[i] = matrix[i][::-1]
    return matrix


M = int(input("Enter M value (more than 5): "))
if M <= 5:
    print("Should be more than 5. Try again.")
else:
    matrix = generate_matrix(M)

    print("Before sorting:")
    print_matrix(matrix)
    print()

    sorted_by_sum = sort_columns(matrix)
    print("After sorting by the sum of the column elements:")
    print_matrix(sorted_by_sum)
    print()

    sorted_odd_even = sort_odd_even(matrix)
    print("After sorting the odd and even columns:")
    print_matrix(sorted_odd_even)
