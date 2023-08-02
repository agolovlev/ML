def sum_num(s):
    print(sum([int(i) for i in str(s) if i.isdigit()]))

sum_num('12345eee')
