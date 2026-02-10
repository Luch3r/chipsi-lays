def print_matrix(matrix):
    for row in matrix:
        print(*row)
    print()


def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def sequential_matrix(n):
    matrix = []
    value = 1
    for i in range(n):
        row = []
        for j in range(n):
            row.append(value)
            value += 1
        matrix.append(row)
    return matrix


def chess_matrix(n):
    return [[(i + j) % 2 for j in range(n)] for i in range(n)]


N = 4

print("Единичная матрица:")
print_matrix(identity_matrix(N))

print("Последовательная матрица:")
print_matrix(sequential_matrix(N))

print("Шахматная матрица:")
print_matrix(chess_matrix(N))
