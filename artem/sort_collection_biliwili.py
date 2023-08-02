bvd = {'Дили': set(), 'Били': set(), 'Вили': set()}
while (string := input()) != 'конец':
    name, comentator = string.split(': ')
    bvd[name] = bvd.get(name) | set([comentator])
for name, comentator in sorted(bvd.items(), key=lambda x: -len(x[1])):
    print(f'Количество уникальных комментаторов у {name} - {len(comentator)}')