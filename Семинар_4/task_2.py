import math

path = 'Task_1.txt'

with open(path, "r", encoding='UTF-8') as data:
    file = data.readline()
    
data_file = file.replace(' = 0', '').replace(' + ', ' ').replace(' - ', ' -').replace('x**2', '').replace('*', '').replace('x', '').split()

print(data_file)

a = int(data_file[0])
b = int(data_file[1])
c = int(data_file[2])

discr = b**2 - 4*a*c

if discr > 0:
    x1 = (-b + math.sqrt(discr))/(2*a)
    x2 = (-b - math.sqrt(discr))/(2*a)
    result = f'x1 = {x1}, x2 = {x2}'
elif discr == 0:
    x = -b/(2*a)
    result = f'x = {x}'
else:
    result = 'Корней нет'

pathWrite = 'X_Task_2.txt'    
with open(pathWrite, "w", encoding='UTF-8') as data:
    data_file = data.write(file + '\n')
    data_file = data.write(result)


