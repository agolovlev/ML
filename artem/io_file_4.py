"""from string import punctuation

def longest_word_in_file(file_name: str) -> str:
    my_file = open(file_name, mode='r', encoding='utf-8')
    all_lines = my_file.read()
    for p in punctuation:
        all_lines = all_lines.replace(p, '')
    all_lines = all_lines.split()
    res, max_len = '', 0
    for i in all_lines:
        if len(i) >= max_len:
            res = i
            max_len = len(i)
    return res

print(longest_word_in_file('test.txt'))"""
"""
my_file = open('numbers.txt', mode='r', encoding='utf-8')
all_lines = my_file.read()
all_lines = all_lines.split()
count3 = summ2 = 0
for i in all_lines:
    lenOfNum = len(i)
    if lenOfNum == 3:
        count3 += 1
    if lenOfNum == 2:
        summ2 += int(i)
print(count3, summ2)

def find_lines_len_more_6(file_name:str) -> int:
    with open(file_name, 'r') as f:
        text = f.read().split('\n')
    count6 = 0
    for line in text:
        if len(line) > 6:
            count6 += 1
    return count6


print(find_lines_len_more_6('test2.txt'))
"""

with open('test3.txt', 'r') as file:
    my_list = file.read().upper().split()
words = dict.fromkeys(my_list, 0)
for key, value in words.items():
    words[key] = my_list.count(key)

"""
with open('test3.txt', encoding='UTF-8') as file:
    print(len(set(file.read().lower().split())))
"""