# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

path_1 = 'Task_4.txt'
path_2 = 'Task_4_1.txt'

with open(path_1, "r", encoding='UTF-8') as data:
    equation_1 = data.readline()

with open(path_2, "r", encoding='UTF-8') as data:
    equation_2 = data.readline()
    
multipliers_1 = []
multipliers_2 = []
degrees_1 = []
degrees_2 = []
mult_string = ''
mult_stop = 0
degr_string = ''
degr_stop = 0

del_start = equation_1.find('>')
equation_1 = equation_1[(del_start + 2):]

while equation_1 != '':
    mult = equation_1.find('X')
    if mult == -1:
        if equation_1[0] == '+':
            for i in range(1, len(equation_1)):
                mult_string += equation_1[i]
            multipliers_1.append(int(mult_string))
            mult_string = ''
        else:
            for i in range(len(equation_1)):
                mult_string += equation_1[i]
            multipliers_1.append(int(mult_string))
            mult_string = ''
        mult_stop = len(equation_1)
    elif mult == 0 or (mult == 1 and equation_1[0] == '+'):
        multipliers_1.append(1)
        mult_stop = mult + 1
    elif mult == 1 and equation_1[0] == '-':
        multipliers_1.append(-1)
        mult_stop = mult + 1
    else:
        for i in range(mult - 1):
            mult_string += equation_1[i]
        multipliers_1.append(int(mult_string))
        mult_string = ''
        mult_stop = mult + 1
    
    equation_1 = equation_1[mult_stop:]
    
    degr_start = equation_1.find('**')
    
    if degr_start == -1 and len(equation_1) > 0:
        degrees_1.append(1)
        degrees_1.append(0)
    elif degr_start != -1:
        if (equation_1.find('+') and equation_1.find('-')) != -1:
            degr_stop = min(equation_1.find('+'), equation_1.find('-'))
        elif equation_1.find('+') == -1:
            degr_stop = equation_1.find('-')
        else:
            degr_stop = equation_1.find('+')
    
        for i in range(degr_start + 2, degr_stop):
            degr_string += equation_1[i]
        degrees_1.append(int(degr_string))
        degr_string = ''
        equation_1 = equation_1[degr_stop:]

print(multipliers_1)
print(degrees_1)