"""import os
print(os.name)

import os
print(os.environ['HOME'])

from string import Template

values = {'one': 'Привет', 'copter': 'Квадракоптер'}

t = Template("
Ну что, мои хорошие, всем $one
Это шаблонная строка
В нее можно вставлять значения по ключам
Хочу сюда вставлю слово $copter, хочу сюда $copter
")

print(t.substitute(values))

from sys import getrecursionlimit
print(getrecursionlimit())
"""
from string import ascii_lowercase
from string import ascii_uppercase
from string import punctuation
print(ascii_lowercase)
print(ascii_uppercase)
print(punctuation)
