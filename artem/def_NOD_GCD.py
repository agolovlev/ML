def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


n = int(input())
inpList = []
for i in range(n):
    inpList.append(int(input()))
minNum = inpList[0]
for i in range(n-1):
    if minNum >= gcd(inpList[i], inpList[i+1]):
        minNum = gcd(inpList[i], inpList[i+1])
print(minNum)
