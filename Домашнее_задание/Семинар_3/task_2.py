# <Задание 2>
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

import random

n = int(input('Сколько чисел будет в списке? : '))
a = int(input('Начальное значение случайных чисел : '))
b = int(input('Конечное значение случайных чисел : '))

numbers_list = []

for i in range(n):
    numbers_list.append(random.randint(a, b))

print(numbers_list)

if n % 2 == 0:
    list_length = n / 2
else:
    list_length = int(n / 2) + 1

new_list = []

for i in range(list_length):
    new_list.append(numbers_list[i] * numbers_list[-i-1])

print(new_list)