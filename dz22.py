# 1. Напишите программу, которая принимает список чисел от пользователя и передает его в функцию modify_list, которая изменяет элементы списка.
# Функция должна умножить нечетные числа на 2, а четные числа разделить на 2. Выведите измененный список на экран.
#
# Объясните, почему изменения происходят только внутри функции и как работают изменяемые и неизменяемые параметры.

# Пример вывода:
# Введите список чисел, разделенных пробелами: 1 2 3 4 5
# Измененный список чисел: [2, 1, 6, 2, 10]

def modify_list(numbers):
    numbers = [int(i) for i in numbers]
    new_list = [i // 2 if i % 2 == 0 else i * 2 for i in numbers]
    return new_list


my_list = input('Введите список чисел, разделенных пробелами: ').split()
print(modify_list(my_list))


# 2. Напишите программу, которая принимает произвольное количество аргументов от пользователя и передает их в функцию calculate_sum,
# которая возвращает сумму всех аргументов. Используйте оператор * при передаче аргументов в функцию. Выведите результат на экран.
#
# Пример вывода:
# Введите числа, разделенные пробелами: 1 2 3 4 5
# Сумма чисел: 15


def calculate_sum(*numbers):
    numbers = [int(i) for i in numbers]
    return sum(numbers)

my_list = input('Введите список чисел, разделенных пробелами: ').split()
print(calculate_sum(*my_list))






# def calculate_sum(*numbers):
#     return sum(numbers)
#
# my_list = '1 2 3 4 5'.split(' ')
#
# my_list = [int(i) for i in my_list]
# print(calculate_sum(*my_list))
