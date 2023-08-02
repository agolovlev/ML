myString1 = input().lower()
myString2 = input().lower()
myDict1,myDict2 = {}, {}
for i in myString1:
    if (i.isalpha()):
        if (i in myDict1):
            myDict1[i] += 1
        else:
            myDict1[i] = 1
for i in myString2:
    if (i.isalpha()):
        if (i in myDict2):
            myDict2[i] += 1
        else:
            myDict2[i] = 1
if myDict1 == myDict2:
    print('YES')
else:
    print('NO')
