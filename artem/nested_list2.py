lst1 = []

for i in range(5):
    lst1.append(list(map(int, input().split())))
    if sum(lst1[i]) > 0 :
        break
for j in range(5):
    if lst1[i][j] == 1:
        print(abs(2-i)+abs(2-j))
        break
