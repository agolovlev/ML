countOfPositions, matrix = 0, []
N, M = map(int,input().split())
matrix = [['.' for col in range(M+2)] for row in range(N+2)]
for i in range(1,N+1):
    matrix[i] = (list(['.']+list(input())+['.']))
for i in range(1,N+1):
    for j in range(1,M+1):
        if matrix[i][j] == matrix[i-1][j] == matrix[i+1][j] == matrix[i][j-1] == matrix[i][j+1] == '.':
            countOfPositions += 1
print(countOfPositions)