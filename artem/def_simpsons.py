def format_name_list(names: list):
    if len(names) == 0:
        return ''
    elif len(names) == 1:
        return names[0]['name']
    else:
        name_list = []
        for i in range(len(names)-1):
            name_list.append(names[i]['name']+',')
        name_list[-1] = name_list[-1][0:-1]
        name_list.append('и')
        name_list.append(names[-1]['name'])
    result = (' '.join(name_list))
    return result


# код ниже не стоит удалять, он нужен для проверки
assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]) == 'Bart, Lisa, Maggie, Homer и Marge'

assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) == 'Bart, Lisa и Maggie'

assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]) == 'Bart и Lisa'

assert format_name_list([{'name': 'Bart'}]) == 'Bart'

assert format_name_list([]) == ''

assert format_name_list([{'name': 'Maggie'}, {'name': 'Lisa'}, {'name': 'Barney'}, {'name': 'Homer'}, {'name': 'Bart'}, {'name': 'Moe'}]) == 'Maggie, Lisa, Barney, Homer, Bart и Moe'

assert format_name_list([{'name': 'Marge'}, {'name': 'Maggie'}, {'name': 'Seymour'}]) == 'Marge, Maggie и Seymour'

assert format_name_list([{'name': 'Maude'}, {'name': 'Bart'}]) == 'Maude и Bart'

print('Проверки пройдены')