# функция merge_two_list должна объединить два списка
def merge_two_list(lst1, lst2):
    lst1 = lst1 + lst2
    listSorted = False
    maxIndex = len(lst1)
    while not listSorted:
        index = 0
        listSorted = True
        while index != (maxIndex - 1):
            if lst1[index] > lst1[index + 1]:
                lst1[index + 1], lst1[index] = lst1[index], lst1[index + 1]
                listSorted = False
            index += 1
    return lst1

# функция merge_sort должна выполнить сортировку
def merge_sort(a):
    if len(a) == 1:
        return a
    left_part = merge_sort(a[0:len(a)//2])
    right_part = merge_sort(a[len(a) // 2::])
    return merge_two_list(left_part, right_part)


n = int(input())
mas = list(map(int,input().split()))
print(*merge_sort(mas))
