def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0):
    "заполнение матрицы"
    matrix = [[0 for _ in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(size):

            if i == j:
                matrix[i][j] = i+1
            elif i > j:
                matrix[i][j] = down_fill
            else:
                matrix[i][j] = up_fill
    return matrix


print(create_matrix(5, 6, 7))
