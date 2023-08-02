"""
def first_repeated_word(string):
    "Находит первый дубль в строке"
    str_list = list(string.split())
    for i in str_list:
        if str_list.count(i) > 1:
            return i
    return None
"""
def first_repeated_word(string):
    "Находит первый дубль в строке"
    str_list = list(string.split())
    str_set = set()
    for i in str_list:
        if i in str_set:
            return i
        else:
            str_set.update({i})
    return None

stri = "ab ca bc Ab cA aB bc"
print(first_repeated_word(stri))