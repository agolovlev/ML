count, n, lst1 = 0, int(input()), list(map(int, input().split()))
for index in range(len(lst1)-1):
    for pos in range(index, -1, -1):
        if lst1[pos+1] < lst1[pos]:
            lst1[pos + 1], lst1[pos] = lst1[pos], lst1[pos + 1]
print(*lst1)


