n, m = map(int, input().split())
A = [[0 for elem1 in range(m)] for elem2 in range(n)]
digit = 0
for i in range(n):
    if i % 2 == 1:
        for j in range(m-1, -1, -1):
            A[i][j] = digit
            digit += 1

    else:
        for j in range(m):
            A[i][j] = digit
            digit += 1

for i in range(n):
    for j in range(m):
        print(A[i][j], end=" ")
    print()