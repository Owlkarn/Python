# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

n = int(input('Введите число: '))

if (n % 10 == 0 or n % 15 == 0) and n % 30 != 0:  #Если число должно быть кратно 5 и 10 одновременно, то можно провести проверку только на 10, т.к. если число кратно 10, то оно кратно и 5.
    print('yes')
else:
    print('no') 