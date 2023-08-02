n, m = map(int, input().split())
triangle = []

for i in range(0, n):
    triangle.append(list(map(int, input().split())))

for i in range(n-2, -1, -1):
    for j in range(m-2, -1, -1):
        triangle[i][j] = triangle[i][j+1] + triangle[i+1][j]

for i in range(n):
    for j in range(m):
        print(triangle[i][j], end=" ")
    print()