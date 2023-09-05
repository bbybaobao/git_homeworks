def generate_matrix(n):
    matrica = []
    for i in range(n):
        row = []
        for j in range(n):
            if i % 2 == 0:
                row.append(str(i + 1))
            else:
                row.append(str(-n + j))
        matrica.append(row)
    return matrica


def print_matrix(matrica):
    max_width = len(str(matrica[-1][-1]))
    for row in matrica:
        for num in row:
            print(f"{num:>{max_width}}", end=" ")
        print()


try:
    N = int(input("Enter matrix size (N): "))
    if N <= 0:
        print("Matrix size must be a positive number.")
    else:
        matrix = generate_matrix(N)
        print("Generated Matrix:")
        print_matrix(matrix)
except ValueError:
    print("Please enter an integer for the size of the matrix.")
