def find_duplicate(lst):
    result_list = []
    for i in lst:
        if (i not in result_list) and (lst.count(i) > 1):
            result_list.append(i)
    return result_list


assert find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]) == [1, 2]
assert find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]) == [2, 1]
assert find_duplicate([1, 2, 3, 4]) == []
assert find_duplicate([8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8]) == [8, 7, 6, 5, 4]
print('Все успешно')