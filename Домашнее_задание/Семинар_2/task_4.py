# Реализуйте алгоритм перемешивания списка, без использования встроеных методов (особенно SHUFFLE, без него) можно (нужно) использовать библиотеку Random


import random

n = int(input('Сколько чисел будет в списке? : '))
a = int(input('Начальное значение случайных чисел : '))
b = int(input('Конечное значение случайных чисел : '))

list = []

for i in range(n):
    list.append(random.randint(a, b))

print(list)

list_shuffle = []

for i in range(n):
    list_shuffle.insert(random.randint(0, n), list[i])
    
print(list_shuffle)


