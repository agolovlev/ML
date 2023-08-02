s = input('Введите строку! Подсчитваем ее буквы: ')
d = {}
for i in s:
     if i.isalpha():
        d[i] = d.get(i, 0) + 1
print(d)
for letter, count in d.items():
    print(letter, count)