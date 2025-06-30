def deco(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))
        return "finished"
    return wrapper


@deco
def my_func(x, exp=2):  # Функция получает какое-то число и возводит его в указанную степень
    return x ** exp


print(my_func(3, 5))
