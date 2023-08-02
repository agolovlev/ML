def reverse(l):
    if len(l) == 0:
        print()
        return []
    print(l[-1], end= ' ')
    return reverse(l[0:-1:])

n = int(input())
mylist = list(map(int, input().split()))
reverse(mylist)
