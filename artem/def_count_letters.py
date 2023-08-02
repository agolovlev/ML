def count_letters(phrase):
    upper = [i for i in phrase if i.isupper()]
    lower = [i for i in phrase if i.islower()]
    print('Количество заглавных символов:', len(upper))
    print('Количество строчных символов:', len(lower))
