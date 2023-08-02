"""my_tuple = (100,)
print(my_tuple * 3)

a = (1,)
b = ('R',)
c = ('A',)
d = (2,)
result = a*3 + 5*b + 8*c + 5*d
print(result)
"""

"""
n = int(input())
print(tuple(i for i in range(n, (n **2) + 1) if i % 2 != 0))

my_tuple = (-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -73, 29)
new_tuple = tuple(i for i in my_tuple if i % 2 != 0)
print(sum(new_tuple)/len(new_tuple))

print(alphabet := {chr(i+96): i for i in range(1,27)})

c1 = {'red': 32, 'blue': 35}
c2 = {'red': 9, 'blue': 10}

print(c1 > c2)

account = {
  "id": 3136,
  "uid": "1359acc6-f07a-4a2a-984e-3fb809982948",
  "account_number": "0847799459",
  "iban": "GB90XTND56373623909314",
  "bank_name": "ABN AMRO HOARE GOVETT CORPORATE FINANCE LTD.",
  "routing_number": "126602476",
  "swift_bic": "BCYPGB2LHGB"
}
keys = list(account)
print(keys)

d1 = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}
d2.update(d1)
print(d2)
my_set = set([1, 2, 2, 2, 2, 1, 1, 2, 2, 1, 2])
print(len(my_set))


print('INGNORE HIM!' if len(set(input()))%2 != 0 else 'CHAT WITH HER!')

my_set = set()
for i in input().lower().split(','):
    print('ДА' if i in my_set else 'НЕТ')
    my_set.add(i)

my_set1 = set(map(int, input().split()))
my_set2 = set(map(int, input().split()))
my_set3 = my_set1 - my_set2
print(*sorted(my_set3))

myNewString = ''
for i in input():
    if i not in myNewString:
        myNewString += i
print(myNewString)


my_frozen = frozenset([int('7'*i) for i in range(1, 78)])

english_words = ('attack', 'bless', 'look', 'reckless', 'short', 'monster', 'trolley', 'sound',
                 'ambiguity', 'researcher', 'trunk', 'coat', 'quantity', 'question', 'tenant',
                 'miner', 'definite', 'kit', 'spectrum', 'satisfied', 'selection', 'carve',
                 'ask', 'go', 'suggest')
words_with_position = [f'Word № {index} = {word}' for index, word in enumerate(english_words,1)]
for i in words_with_position:
    print(i)


def say_hello_world(s):
    print(s, 'говорит hello world!')



def square(x):
    print(x**2)

a = square(6)
print(a)

# объявление функции
def repeat_please_n_times(n):
    print(*['Just do it' for i in range(n)], sep='\n')

repeat_please_n_times(5)

# объявление функции
# объявление функции
def print_initials(name, surname, middlename):
    print(surname.title(), name[0].upper() + '.' + middlename[0].upper() + '.')

# считываем данные
name = input()
surname = input()
middlename = input()

# вызываем функцию
print_initials(name, surname, middlename)


def factorial(n):
    f = 1
    for i in range(2,n+1):
        f *= i
    return 1 if f == 0 else f


n=int(input())
print(factorial(n))

value = 10


def foo():
    value += 1

foo()
print(value)

напечатай = print
максимум = max
отсортируй = sorted
мой_список = [1,2,3,4,5]
мой_отсортированный_список = отсортируй(мой_список)
напечатай(отсортируй(мой_список))
напечатай(максимум(мой_список))
"""

def color() -> None:
    g = 'green'

    def grey() -> None:
        nonlocal g
        g = 'grey'
        print(g)

    grey()
    print(g)


color()