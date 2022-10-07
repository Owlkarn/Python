# <Задание 1>
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# [2, 3, 5, 9, 3] => на нечётных позициях элементы 3 и 9, ответ: 12

import random

n = int(input('Сколько чисел будет в списке? : '))
a = int(input('Начальное значение случайных чисел : '))
b = int(input('Конечное значение случайных чисел : '))

numbers_list = []

for i in range(n):
    numbers_list.append(random.randint(a, b))

print(numbers_list)

sum_numbers = 0

for i in range(1, n, 2):
    sum_numbers += numbers_list[i]

print(sum_numbers)

