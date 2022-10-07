elem = input('Введите элемент для поиска: ')
n = int(input('В скольки элементах будем искать? : '))
test_list = []

for i in range(n):
    test_list.append(input(f'Введите {i+1} элемент: '))
    
cons = True

for i in range(n):
    if test_list[i] == elem and i != n-1:
        for j in range(i+1, n):
            if test_list[j] == elem:
                print(f'- список: {test_list}, ищем: {elem}, ответ: {j}')
                cons = False

if cons:
    print(f'- список: {test_list}, ищем: {elem}, ответ: -1')           
