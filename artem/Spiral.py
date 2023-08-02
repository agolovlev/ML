n = int(input())
incXY = [[1, 0], [0, 1], [-1, 0], [0, -1]]
x = y = dirr = 0
k = m = 0
matrix = [[-1 for i in range(n)] for j in range(n)]
for i in range(n ** 2):
    if dirr == 0 and (x == (n - 1) or matrix[x + 1][y] != -1):
        dirr = 1
    elif dirr == 1 and (y == (n - 1) or matrix[x][y + 1] != -1):
        dirr = 2
    elif dirr == 2 and (x == 0 or matrix[x - 1][y] != -1):
        dirr = 3
    elif dirr == 3 and (y == 0 or matrix[x][y - 1] != -1):
        dirr = 0
    matrix[x][y] = i + 1
    x += incXY[dirr][0]
    y += incXY[dirr][1]

for k in range(n):
    for m in range(n):
        print(matrix[m][k], end=' ')
    print()
print()
