n = int(input())
logins = {}
for i in range(n):
    str1 = input()
    newLogin = str1
    k = 0
    while newLogin in logins:
        k += 1
        newLogin = str1 + str(k)
    logins.setdefault(newLogin)
    print('OK' if str1 == newLogin else newLogin)
