# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

n = input('Введите последовательность цифр: ')

count = 0
solo_numbers = list(filter(lambda x: (n.count(x) == 1), n))

# for i in n:
#     if n.count(i) == 1:
#         solo_numbers.append(i)
    
print(solo_numbers)