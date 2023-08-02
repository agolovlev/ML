def print_goods(*args):
    no_items = True
    for num, value in enumerate([i for i in args if isinstance(i, str) and i != '']):
        print(f'{num+1}. {value}')
        no_items = False
    if no_items:
        print('Нет товаров')


print_goods(1, True, 'Грушечка', '', 'Pineapple')