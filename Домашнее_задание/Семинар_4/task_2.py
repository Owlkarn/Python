# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите натуральное число: '))

easy_mult = 2
easy_mult_numbers = []

while n/easy_mult != 1:
    if n % easy_mult == 0:
        easy_mult_numbers.append(easy_mult)
        n = n/easy_mult
    else:
        easy_mult += 1
        
easy_mult_numbers.append(int(n))
print(easy_mult_numbers)