matrix1 = []
n, m = map(int,input().split())
atAll = 0
for i in range(n):
    matrix1.append(list(input()))
    if 'S' not in matrix1[i]:
        matrix1[i] = ['x' for i in range(m)]
matrix1 = list(zip(*matrix1))
for i in range(m):
    if 'S' not in matrix1[i]:
        matrix1[i] = ['x' for i in range(n)]
for i in range(m):
    atAll += matrix1[i].count('x')
print(atAll)
