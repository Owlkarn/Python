# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число: '))
prod = 1
for i in range(1, n+1):
    prod *= i
    
print(prod)