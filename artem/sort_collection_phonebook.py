phonebook = {}
for i in range(int(input())):
    num, name = input().split()
    phonebook[name] = phonebook.get(name,[]) + [num]
for i in range(int(input())):
    print(*phonebook.get(input(), ["Неизвестный номер"]))


