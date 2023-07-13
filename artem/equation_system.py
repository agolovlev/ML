n, m = map(int, input().split())
# print(m,n)
counter = 0
for a in range(n):
    for b in range(m):
        if (a ** 2 + b == n) and (b ** 2 + a == m):
            counter += 1
print(counter)