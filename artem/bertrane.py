n, simpleCount = int(input()), 0
startWith = n + 1
if startWith % 2 == 0:
    startWith += 1
for i in range(startWith, 2 * n, 2):
    cnt = 0
    if (i > 11) and ((i % 5 == 0) or (i % 3 == 0) or (i % 7 == 0) or (i % 11 == 0)):
        # print(i)
        continue
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            cnt += 1
            break
    if cnt == 0:
        simpleCount += 1
print(simpleCount)
