def fact(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fact(n-2) * n

print(fact(0))