# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите координату X: '))
y = int(input('Введите координату Y: '))

if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif x > 0 and y < 0:
    print('4')
elif x == 0 and y != 0:                    # Сделал для условия "(или на какой оси она находится)". Если нужно чтобы переменные не были равны 0, то добавляется в начале проверка на 0.
    print('Точка находится на оси X')
elif x != 0 and y == 0:
    print('Точка находится на оси Y')
else:
    print('Точка находится в начале координат')