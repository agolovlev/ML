card_number = reversed(input())
summ = 0
for index, value in enumerate(card_number):
    value = int(value)
    if index % 2 == 0:
        summ += value
    else:
        value *= 2
        if value >= 10:
            value = value - 9
        summ += value
if summ % 10 == 0:
    print(True)
else:
    print(False)
