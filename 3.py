import random

N, M = 4, 5
matrix = [[random.randint(-50, 50) for _ in range(M)] for _ in range(N)]

print("Случайная матрица:")
print_matrix(matrix)

max_val = matrix[0][0]
min_val = matrix[0][0]
max_pos = min_pos = (0, 0)

positive = negative = zeros = 0

for i in range(N):
    for j in range(M):
        value = matrix[i][j]

        if value > max_val:
            max_val = value
            max_pos = (i, j)

        if value < min_val:
            min_val = value
            min_pos = (i, j)

        if value > 0:
            positive += 1
        elif value < 0:
            negative += 1
        else:
            zeros += 1

print(f"Максимальный элемент: {max_val}, позиция: {max_pos}")
print(f"Минимальный элемент: {min_val}, позиция: {min_pos}")
print(f"Положительных: {positive}")
print(f"Отрицательных: {negative}")
print(f"Нулевых: {zeros}")
