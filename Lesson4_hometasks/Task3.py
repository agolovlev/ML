def amulet_area(a, b, c):
    # your code here
    p = (a + b + c)/2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return S

assert amulet_area(3, 4, 5) == 6

summ = 0
a = [int(i) for i in input().split()]
for i in a:
    summ += i
print(summ)
