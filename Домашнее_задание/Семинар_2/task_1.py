# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# НЕОБЯЗАТЕЛЬНО Попробовать решить не переводя числа в строку
# Пример:
# 6782 -> 23
# 0,56 -> 11

import math
from decimal import Decimal
n = Decimal(input('Введите число: '))
while  n % 10 != 0:
    n = n * 10

length = int(math.log10(n))
i = 0
summ = 0

while i < length:
    summ += (int(n / 10**(length - i)) % 10) 
    i+=1

print (summ)

