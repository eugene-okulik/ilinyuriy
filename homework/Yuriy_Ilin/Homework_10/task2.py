# Спасибо, благодаря этому заданию я узнал как ведет себя комп, когда улетает
# в бесконечную рекурсию :D

def deco(func):
    def wrapper(s, count = 1):
        for _ in range(count):
            func(s)
    return wrapper


@deco
def my_func(s):
    print(s)


my_func('Hello', 3)
