def calculate(x: float, y: float, operation: str = 'a') -> None:
    def addition(x, y):
        print(x + y)
        return None

    def substraction(x, y):
        print(x - y)
        return None

    def division(x, y):
        if y == 0:
            print('На ноль делить нельзя!')
        else:
            print(x / y)
        return None

    def multiplication(x, y):
        print(x * y)
        return None

    match operation:
        case 'a':
            addition(x, y)
        case 's':
            substraction(x, y),
        case 'd':
            division(x, y),
        case 'm':
            multiplication(x, y)
        case _:
            print('Ошибка. Данной операции не существует')

#calculate(4.0, 0.0, 'd')
