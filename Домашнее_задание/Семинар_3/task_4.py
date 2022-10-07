# <Задание 4>
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# 45 => 101101
# 3 => 11
# 2 => 10

n = int(input('Введите число: '))

list_double = []

while n != (0 or 1):
    list_double.insert(0, n % 2)
    n = int(n / 2)

if n == 1:
    list_double.insert(0, n)

for i in list_double:
    print(i, end='')