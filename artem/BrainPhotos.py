n, m = map(int,input().split())
matrix = [list(input().split()) for j in range(n)]
for i in matrix:
    if i[0] in 'CMY':
        print('#Color')
        break
else:
    print('#Black&White')
