# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Сколько чисел? : '))
list = []
for i in range(-n, n+1):
    list.append(i)
print(list)

path = "file_task_1.txt"
data = open(path, 'r')
numbers = []

for i in data:
    numbers.append(list[int(i)])
    
print(numbers[0] * numbers[1])