# 1. Напишите функцию merge_dicts, которая принимает произвольное количество словарей в качестве аргументов и возвращает новый словарь,
# объединяющий все входные словари. Если ключи повторяются, значения должны быть объединены в список.
# Функция должна использовать аргумент **kwargs для принятия произвольного числа аргументов словаря.
#
#
# Пример ввода:
#
# {'a': 1, 'b': 2}
#
# {'b': 3, 'c': 4}
#
# {'c': 5, 'd': 6}
#
#
# Пример вывода:
#
#
# {'a': [1], 'b': [2, 3], 'c': [4, 5], 'd': [6]}

my_dict = {"name": "John", "age": 25, "city": "New York"}

# print(my_dict)
# print(list(my_dict.items()))
# print(list(my_dict.keys()))
# print(list(my_dict.values()))

print('-' * 50)
for item in my_dict:
    print(my_dict[item])

print('-' * 50)
for item in my_dict.values():
    print(item)

print('-' * 50)
for item in my_dict.keys():
    print(item)

print('-' * 50)
for key, value in my_dict.items():
    print('key:', key)
    print('value:', value)