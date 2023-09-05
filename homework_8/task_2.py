import random

N = int(input("Enter matrix size (N): "))
if N <= 0:
    print("Matrix size must be a positive number.")
else:
    matrix = [[random.randint(1, 100) for _ in range(N)] for _ in range(N)]

    for row in matrix:
        print(" ".join(map(str, row)))

    diagonal_sum = sum(matrix[i][i] for i in range(N))
    print(f"Diagonal sum of numbers: {diagonal_sum}")

    last_column_sum = sum(row[N - 1] for row in matrix)
    print(f"Sum of numbers in last column: {last_column_sum}")
