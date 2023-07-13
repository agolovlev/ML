count, n, lst1 = 0, int(input()),list(map(int, input().split()))
listSorted = False
maxIndex = len(lst1)
while not listSorted:
    index = 0
    listSorted = True
    for index in range(maxIndex):
        if lst1[index] > lst1[index+1]:
            count += 1
            tmp = lst1[index]
            lst1[index] = lst1[index+1]
            lst1[index+1] = tmp
            listSorted = False
print(*lst1)
print(count)