size = int(input())
A, B, C = map(int, input().split())
for i in range(size):
    print(' '.join((str(B))*i+str(C)+(str(A))*(size-i-1)))


