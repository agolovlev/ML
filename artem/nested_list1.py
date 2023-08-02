#matrx = ['BBWB', 'BBWB', 'WWBW', 'BBWB']
errors, matrix1, matrix2  = 0, [], []

n, m = map(int,input().split())
for i in range(n):
    matrix1.append(input())


for i in range(n):
    matrix2.append(input())
    for j in range(m):
        if matrix1[i][j] == matrix2[i][j]:
            errors += 1
print(errors)
