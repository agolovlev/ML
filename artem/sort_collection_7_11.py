"""
Sony PlayStation 5: 46000
Телевизор QLED Samsung QE65Q60TAU: 87090
Смартфон Samsung Galaxy A11: 10000
Планшет Samsung Galaxy Tab S6: 26600
конец
"""
list_of_poducts = []
while (new_str := input().split(sep=': ')) != ['конец']:
    list_of_poducts += [new_str]
for i in sorted(list_of_poducts, key=lambda x: x[1]):
    print(*i)