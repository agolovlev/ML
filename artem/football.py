matchesNum, commandColor, n = 0, [], int(input())
for i in range(n):
    commandColor.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if commandColor[i][0] == commandColor[j][1]:
            matchesNum += 1
print(matchesNum)