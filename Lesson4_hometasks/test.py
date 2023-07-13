ai = 0
aj = 0
aa, bb, cc = [], [], []
k = 0
while True:
    aa = [i for i in input().split()]
    if aa[0] == 'end':
        break
    bb.append(aa.copy())
    cc.append(aa.copy())

len_i = len(bb)
len_j = len(bb[0])

for i in range(len_i):
    for j in range(len_j):
        cc[i][j] = 0
for i in range(len_i):
    for j in range(len_j):
        for d in range(-1,2,2):
            ai = i + d
            aj = j
            if ai == -1:
                ai = len_i-1
            elif ai == len_i:
                ai = 0
            cc[i][j] = int(cc[i][j])+int(bb[ai][aj])
            ai = i
            aj = j + d
            if aj == -1:
                aj = len_j-1
            elif aj == len_j:
                aj = 0
            cc[i][j] = int(cc[i][j])+int(bb[ai][aj])
        print(cc[i][j], end=' ')
    print()


#  1  2  3
#  4  5  6
#  7  8  9