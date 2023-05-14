def share_bread(N, K):
    # your code here
    x = int(K / N)
    y = K - N * int(K / N)
    print(x,y)
    return x, y


# если в функции всё верно, то после выполнения этой строчки, не должно выскакивать ошибок
assert share_bread(N=3, K=14) == (4, 2)