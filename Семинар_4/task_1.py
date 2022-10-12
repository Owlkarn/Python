import random
size = random.randint(5,10)

string = ''
path = r'Task_1.txt'

for _ in range(size):
    string += f'{random.randint(1, 9999)} '
    
print(string[:-1])

with open(path, "w", encoding='UTF-8') as data:
    data.write(string[:-1])
    
with open(path, "r", encoding='UTF-8') as data:
    file = data.readline()
    
file = file.split()

for i in range(len(file)):
    file[i] = int(file[i])
    
print(min(file), max(file), sep='=>')

