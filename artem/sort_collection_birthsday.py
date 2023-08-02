birthdays = {}
for i in range(int(input())):
    name, date, month = input().split()
    birthdays[month] = birthdays.get(month, []) + [name]
for i in range(int(input())):
    print(*birthdays.get(input(), ["Нет данных"]))
