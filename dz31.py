#1. Напишите программу, которая генерирует и выводит квадраты чисел от 1 до N с использованием генераторного выражения.
# Реализуйте функцию generate_squares, которая принимает число N в качестве аргумента и
# использует генераторное выражение для генерации квадратов чисел.
# Затем выведите квадраты чисел на экран.

# Пример работы программы:
#
# 1
# 4
# 9
# 16
# 25


def generate_squares(n):
    return (i ** 2 for i in range(1, n + 1))


x = int(input('Число: '))
for i in generate_squares(x):
    print(i)


def generate_squares2():
    count1 = 0
    count2 = 1
    for i in range(x):
        yield count1
        count1, count2 = count2, count1 + count2


gen = generate_squares2()
x = int(input('Число: '))
[print(next(gen)) for i in range(x)]
