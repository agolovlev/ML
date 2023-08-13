def repeater(func):
    def inner(*args):
        func(*args)
        func(*args)
    return inner

@repeater
def simple_func():
    print('I just simple python func')

simple_func()