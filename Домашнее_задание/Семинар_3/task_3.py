# <Задание 3>
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов. Если число целое, то его дробная часть не считается за 0 и оно (число) в сравнении не участвует

# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

n = int(input('Сколько чисел будет в списке? : '))
a = float(input('Начальное значение случайных чисел : '))
b = float(input('Конечное значение случайных чисел : '))

numbers_list = []

for i in range(n):
    numbers_list.append(round(random.uniform(a, b), 2))

print(numbers_list)

for i in numbers_list:
    if i % 1 != 0:
        min_rem = i
        break

max_rem = numbers_list[0] % 1

for i in numbers_list:
    if min_rem > i % 1 and i % 1 != 0:
        min_rem = i % 1

for i in numbers_list:
    if max_rem < i % 1 and i % 1 != 0:
        max_rem = i % 1
print(round(max_rem, 2), round(min_rem, 2))
print(round((max_rem - min_rem), 2))

