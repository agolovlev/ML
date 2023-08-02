taxists = {}

while (string := input()) != 'конец':
    name, mark = string.split(',')
    taxists[name] = taxists.get(name, []) + [int(mark)]

for name, mark in taxists.items():
    taxists[name] = sum(mark)/ len(mark)

for name, mark in sorted(taxists.items(), key= lambda x: (-x[1], x[0])):
    print(name, mark)

