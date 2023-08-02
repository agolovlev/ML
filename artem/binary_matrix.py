d = {'S': 0, '.': 1}
n, m = map(int, input().split())
matrix = [[d[i] for i in input()] for _ in range(n)]
print(matrix)