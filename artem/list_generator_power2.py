n, m = map(int, input().split())
if n < m:
    print([i**2 for i in range(n,m+1)])
else:
    print([i ** 3 for i in range(n, m-1, -1)])
