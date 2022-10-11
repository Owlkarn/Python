# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

import random

k = int(input('Введите натуральную степень: '))

numbers = []
pathWrite = 'Task_4_1.txt'

with open(pathWrite, 'w', encoding='UTF-8') as data:
    data.write(f'k = {k} -> ')
    
for i in range(k + 1):
    numbers.append(random.randint(-100, 100))

if numbers[0] == 1:
    with open(pathWrite, 'a', encoding='UTF-8') as data:
        data.write(f'X**{k}')  
elif numbers[0] == -1:
    with open(pathWrite, 'a', encoding='UTF-8') as data:
        data.write(f'-X**{k}')
else:
    with open(pathWrite, 'a', encoding='UTF-8') as data:
        data.write(f'{numbers[0]}*X**{k}')   

for i in range(1, len(numbers)):
    if i - k == 0:
        if numbers[i] > 0:
            with open(pathWrite, 'a', encoding='UTF-8') as data:
                data.write(f'+{numbers[i]}')
        elif numbers[i] < 0:
            with open(pathWrite, 'a', encoding='UTF-8') as data:
                data.write(f'{numbers[i]}')
    elif k - i == 1:
        if numbers[i] > 0:
            if numbers[i] == 1:
                with open(pathWrite, 'a', encoding='UTF-8') as data:
                    data.write(f'+X')
            else:
                with open(pathWrite, 'a', encoding='UTF-8') as data:
                    data.write(f'+{numbers[i]}*X')
        elif numbers[i] < 0:
            if numbers[i] == -1:
                with open(pathWrite, 'a', encoding='UTF-8') as data:
                    data.write(f'-X')
            else:
                with open(pathWrite, 'a', encoding='UTF-8') as data:
                    data.write(f'{numbers[i]}*X')
    else:
        if numbers[i] > 0:
            if numbers[i] == 1:
                with open(pathWrite, 'a', encoding='UTF-8') as data:
                    data.write(f'+X**{k - i}')
            else:
                with open(pathWrite, 'a', encoding='UTF-8') as data:
                    data.write(f'+{numbers[i]}*X**{k - i}')
        elif numbers[i] < 0:
            if numbers[i] == -1:
                with open(pathWrite, 'a', encoding='UTF-8') as data:
                    data.write(f'-X**{k - i}') 
            else:
                with open(pathWrite, 'a', encoding='UTF-8') as data:
                    data.write(f'{numbers[i]}*X**{k - i}')    
        else:
            i +=1


