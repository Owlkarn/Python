# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

path_1 = 'Task_4.txt'
path_2 = 'Task_4_1.txt'

def Separate(equation, multipliers, degrees):
    mult_string = ''
    mult_stop = 0
    degr_string = ''
    degr_stop = 0
    
    while equation != '':
        mult = equation.find('X')
        if mult == -1:
            if equation[0] == '+':
                for i in range(1, len(equation)):
                    mult_string += equation[i]
                multipliers.append(int(mult_string))
                mult_string = ''
            else:
                for i in range(len(equation)):
                    mult_string += equation[i]
                multipliers.append(int(mult_string))
                mult_string = ''
            mult_stop = len(equation)
        elif mult == 0 or (mult == 1 and equation[0] == '+'):
            multipliers.append(1)
            mult_stop = mult + 1
        elif mult == 1 and equation[0] == '-':
            multipliers.append(-1)
            mult_stop = mult + 1
        else:
            for i in range(mult - 1):
                mult_string += equation[i]
            multipliers.append(int(mult_string))
            mult_string = ''
            mult_stop = mult + 1
    
        equation = equation[mult_stop:]
    
        degr_start = equation.find('**')
    
        if degr_start == -1 and len(equation) > 0:
            degrees.append(1)
            degrees.append(0)
        elif degr_start != -1:
            if equation.find('+', 1) != -1 and equation.find('-', 1) != -1:
                degr_stop = min(equation.find('+', 1), equation.find('-', 1))
            elif equation.find('+', 1) == -1:
                degr_stop = equation.find('-', 1)
            else:
                degr_stop = equation.find('+', 1)
    
            for i in range(degr_start + 2, degr_stop):
                degr_string += equation[i]
            degrees.append(int(degr_string))
            degr_string = ''
            equation = equation[degr_stop:]

with open(path_1, "r", encoding='UTF-8') as data:
    equation_1 = data.readline()

with open(path_2, "r", encoding='UTF-8') as data:
    equation_2 = data.readline()
    
multipliers_1 = []
multipliers_2 = []
degrees_1 = []
degrees_2 = []

del_start = equation_1.find('>')
equation_1 = equation_1[(del_start + 2):]

del_start = equation_2.find('>')
equation_2 = equation_2[(del_start + 2):]

print(equation_1)
print(equation_2)

Separate(equation_1, multipliers_1, degrees_1)
Separate(equation_2, multipliers_2, degrees_2)

print(multipliers_1)
print(degrees_1)

print(multipliers_2)
print(degrees_2)

keys_degrees = []
keys_degrees.extend(degrees_1)

for i in range(len(degrees_2)):
    solo = True
    for j in range(len(keys_degrees)):
        if degrees_2[i] == keys_degrees[j]:
            solo = False
    if solo:
        keys_degrees.append(degrees_2[i])

keys_degrees.sort(reverse=True)
        
dic_equation_1 = {}
for i in range(len(multipliers_1)):
    dic_equation_1[degrees_1[i]] = multipliers_1[i]

dic_equation_2 = {}
for i in range(len(multipliers_2)):
    dic_equation_2[degrees_2[i]] = multipliers_2[i]
    
equation_3 = []
for i in range(len(keys_degrees)):
    equation_3.append(dic_equation_1.get(keys_degrees[i], 0) + dic_equation_2.get(keys_degrees[i], 0))

print(equation_3)

k = len(equation_3) - 1

pathWrite = 'Task_5.txt'

with open(pathWrite, 'w', encoding='UTF-8') as data:
    data.write(f'k = {k} -> ')

if equation_3[0] == 1:
    with open(pathWrite, 'a', encoding='UTF-8') as data:
        data.write(f'X**{k}')  
elif equation_3[0] == -1:
    with open(pathWrite, 'a', encoding='UTF-8') as data:
        data.write(f'-X**{k}')
else:
    with open(pathWrite, 'a', encoding='UTF-8') as data:
        data.write(f'{equation_3[0]}*X**{k}')   

for i in range(1, len(equation_3)):
    if i - k == 0:
        if equation_3[i] > 0:
            with open(pathWrite, 'a', encoding='UTF-8') as data:
                data.write(f'+{equation_3[i]}')
        elif equation_3[i] < 0:
            with open(pathWrite, 'a', encoding='UTF-8') as data:
                data.write(f'{equation_3[i]}')
    elif k - i == 1:
        if equation_3[i] > 0:
            if equation_3[i] == 1:
                with open(pathWrite, 'a', encoding='UTF-8') as data:
                    data.write(f'+X')
            else:
                with open(pathWrite, 'a', encoding='UTF-8') as data:
                    data.write(f'+{equation_3[i]}*X')
        elif equation_3[i] < 0:
            if equation_3[i] == -1:
                with open(pathWrite, 'a', encoding='UTF-8') as data:
                    data.write(f'-X')
            else:
                with open(pathWrite, 'a', encoding='UTF-8') as data:
                    data.write(f'{equation_3[i]}*X')
    else:
        if equation_3[i] > 0:
            if equation_3[i] == 1:
                with open(pathWrite, 'a', encoding='UTF-8') as data:
                    data.write(f'+X**{k - i}')
            else:
                with open(pathWrite, 'a', encoding='UTF-8') as data:
                    data.write(f'+{equation_3[i]}*X**{k - i}')
        elif equation_3[i] < 0:
            if equation_3[i] == -1:
                with open(pathWrite, 'a', encoding='UTF-8') as data:
                    data.write(f'-X**{k - i}') 
            else:
                with open(pathWrite, 'a', encoding='UTF-8') as data:
                    data.write(f'{equation_3[i]}*X**{k - i}')    
        else:
            i +=1
