def deco(func):
    def wrapper(first, second, operation=None):
        if first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif first < 0 or second < 0:
            return func(first, second, '*')
        else:
            if second == 0:
                return 'Деление на ноль запрещено!'
            return func(first, second, '/')
    return wrapper


@deco
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    else:
        operation == '/'
        return first / second


first = int(input())
second = int(input())

print(calc(first, second))
