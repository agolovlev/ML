n = int(input())
actors = [(input()+',я1').split('я') for i in range(n)]
actors_dict = dict()
for name in actors:
    if name[0] in actors_dict:
        actors_dict[name[0]] += 1
    else:
        actors_dict[name[0]] = 1
a = sorted(actors_dict.items(), key=lambda x: x[1])
print(*a[0])
print(*a[-1])

#print((a:=min(actors_dict, key=lambda x: x[1]))+',',actors_dict[a])
#print((a:=max(actors_dict, key=lambda x: x[1]))+',',actors_dict[a])
