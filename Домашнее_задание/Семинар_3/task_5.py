# <Задание 5>
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] (Негафибоначчи)

n = int(input('Введите число: '))

fibonachi = [0, 1]

for i in range(n - 1):
    fibonachi.append(fibonachi[i] + fibonachi[i + 1])

fibonachi.insert(0, 1)

for _ in range(n - 1):
    fibonachi.insert(0, (fibonachi[1] - fibonachi[0]))

print(fibonachi)