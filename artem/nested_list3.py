n = int(input())
lst2, lst1 = [], []
for i in range(n):
    lst1.append(list(map(int, input().split())))

lst2 = zip(*lst1)
lst2 = [list(row) for row in lst2]
if lst1 == lst2:
    print('Yes')
else:
    print('No')
