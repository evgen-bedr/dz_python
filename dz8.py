# Напишите программу, принимающую число с плавающей точкой и округляющую его до целого числа в соответствии с правилами школьной математики.
# Использовать модуль math и методы из него нельзя. Учесть, что программа должна корректно работать с отрицательными числами.


n = float(input('Введите вещественное число: '))

if n > 0:
    if n - int(n) >= 0.5:
        print('Округленное значение: ', int(n) + 1)
    else:
        print('Округленное значение: ', int(n))
else:
    if n - int(n) <= -0.5:
        print('Округленное значение: ', int(n) - 1)
    else:
        print('Округленное значение: ', int(n))
print('\n')

# 1. Напишите программу, которая запрашивает у пользователя натуральное десятичное число и выводит его двоичное представление.
# Реализуйте алгоритм перевода числа в двоичную систему счисления, используя основные концепции представления чисел (подсказка: через деление с остатком).
# Выведите полученное представление числа на экран.

num1 = int(input('Введите натуральное десятичное число: '))
b = []
while num1:
    num1, num2 = num1 // 2, num1 % 2
    b.append(num2)
b.reverse()
print('Двоичное представление числа:', ''.join(map(str, b)))
