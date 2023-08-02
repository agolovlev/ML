def first_unique_char(s):
    s = s[::-1]
    poss = 0
    for i in s:
        if s.count(i) == 1:
            poss = len(s) - s.index(i) - 1
    return -1 if poss == 0 else poss


s = input()
print(first_unique_char(s))