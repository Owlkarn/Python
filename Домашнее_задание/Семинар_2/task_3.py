# Задайте список из n чисел последовательности (1+1/n)^n
# Выведитте на экран саму последовательность и сумму элеементов этой последовательности (для проверки сумма для 4 элементов = 9,06 (примерно))

n = int(input('Введите число: '))
sum = 0
for i in range(1, n+1):
    sum += (1 + 1/i)**i
    
print(sum)