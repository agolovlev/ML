n, x = map(int, input().split())
multy = []
for i in range(n**2):
    multy.append(((i // n) + 1) * ((i % n) + 1))
print(multy.count(x))
