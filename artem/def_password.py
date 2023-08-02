def check_password(pas):
    upper = [i for i in pas if i.isupper()]
    digits = [i for i in pas if i.isdigit()]
    special = [i for i in '!@#$%*' if i in pas]
    if len(pas) >= 10 and len(upper) > 0 and len(digits) > 2 and len(special) >= 1:
        print('Perfect password')
    else:
        print('Easy peasy')

