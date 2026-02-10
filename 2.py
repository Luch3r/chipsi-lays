def add_matrices(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))


def multiply_by_number(matrix, k):
    return [[element * k for element in row] for row in matrix]


def row_and_column_sums(matrix):
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0]))]
    return row_sums, col_sums


A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

print("Сложение матриц:")
print_matrix(add_matrices(A, B))

print("Транспонирование матрицы A:")
print_matrix(transpose_matrix(A))

print("Умножение матрицы A на число 3:")
print_matrix(multiply_by_number(A, 3))

row_sums, col_sums = row_and_column_sums(A)
print("Суммы строк:", row_sums)
print("Суммы столбцов:", col_sums)
print()
