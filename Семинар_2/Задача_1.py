# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81

NumberN = int(input('Введите число N: '))
result = []
for i in range(NumberN):
    result.append((-3)**i)
print(result)


# for i in range(NumberN):
#     print(pow(-3, i), end=", ")