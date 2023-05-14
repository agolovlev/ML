def amulet_area(a, b, c):
    # your code here
    p = (a + b + c)/2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return S

assert amulet_area(3, 4, 5) == 6