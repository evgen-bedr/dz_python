def validate_args(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], int):
            raise TypeError(f"Аргумент {args[0]} имеет неправильный тип {type(args[0])}. Ожидается <class 'int'>.")
        if not isinstance(args[1], str):
            raise TypeError(f"Аргумент {args[1]} имеет неправильный тип {type(args[1])}. Ожидается <class 'str'>.")
        return func(*args, **kwargs)

    return wrapper


@validate_args
def greet(age, name):
    print(f"Привет, {name}! Тебе {age} лет.")


try:
    greet("25", "Анна")
except TypeError as e:
    print(e)

# ------------------------------------------------------------------------------------


from logging import basicConfig
from logging import info
from logging import INFO

basicConfig(filename='log.txt', level=INFO, format='%(message)s', encoding='utf-8')


def my_logging(func):
    def wrapper(*args):
        res = func(*args)
        info(f'Аргументы {args}, результат {res}')

    return wrapper


@my_logging
def add(a, b):
    return a + b


add(2, 3)
add(5, 7)
