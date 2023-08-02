year = int(input())+1
yearSet = set(int(i) for i in set(str(year)))
while len(yearSet) < 4:
    year += 1
    yearSet = set(int(i) for i in set(str(year)))
print(year)