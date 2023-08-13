with open('test3.txt', 'r') as file:
    my_list = file.read().upper().split()
words = dict.fromkeys(my_list, 0)
for key, value in words.items():
    words[key] = my_list.count(key)
