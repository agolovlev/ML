myList = list(map(int,input().split()))
print(myList)
myDict = {myList[-2]: myList[-1]}
i = len(myList)-3
while i >= 0:
    myDict = {myList[i]: myDict}
    i -= 1
print(myDict)