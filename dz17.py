# Напишите программу, которая принимает два числа и возвращает их сумму и произведение в виде кортежа (sum, product).
# Используйте функцию для вычисления суммы и произведения. Выведите результат на экран с помощью команды print.

# Пример вывода:
# Введите первое число: 3
# Введите второе число: 4
# Сумма и произведение чисел: (7, 12)

def my_funk(a, b):
    summ = a + b
    product = a * b
    return summ, product


print(my_funk(int(input('Введите первое число: ')), int(input('Введите второе число: '))))


# Напишите программу, которая принимает список чисел и возвращает сумму, минимальное и максимальное значение из списка.
# Используйте функцию для обработки списка чисел и возврата трех значений. Выведите результат на экран с помощью команды print.
#
# Пример вывода:
# Введите числа:  3, 7, 2, 9, 1, 5
# Сумма чисел: 27
# Минимальное значение: 1
# Максимальное значение: 9

def my_funk_list(a):
    a = [int(i.strip()) for i in a]
    summ = sum(a)
    num_min = min(a)
    num_max = max(a)
    return summ, num_min, num_max


my_list = input('Введите числа через запятую: ').split(',')

print('Сумма чисел:', my_funk_list(my_list)[0])
print('Минимальное значение:', my_funk_list(my_list)[1])
print('Максимальное значение:', my_funk_list(my_list)[2])