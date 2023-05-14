def leap_year(year):
    # your code here
    if not (year/100 == int(year/100)):
        if (year/4 == int(year/4)):
            return 'YOU SHALL PASS'
    return 'YOU SHALL NOT PASS'

assert leap_year(101) == 'YOU SHALL NOT PASS'