strings = ['This is a string',
                         'test String',
                         'test',
                         'string']
my_dict = {}
for i in range(len(strings)):
    for word in strings[i].lower().split():
        if word in my_dict:
            my_dict[word].append(i)
        else:
            my_dict |= {word: [i]}
        print(word, i)
print(my_dict)
"""
get_word_indices(['This is a string',
                         'test String',
                         'test',
                         'string'])
#{'this': [0], 'is': [0], 'a': [0], 'string': [0, 1, 3], 'test': [1, 2]}
"""