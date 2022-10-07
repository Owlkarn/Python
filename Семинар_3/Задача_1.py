elem = input('Введите элемент для поиска: ')
n = int(input('В скольки элементах будем искать? : '))
test_list = []

for i in range(n):
    test_list.append(input(f'Введите {i+1} элемент: '))
    
print(test_list)

for i in test_list:
    if i.find(elem) != -1:
        print(f'В строке под индексом {i} найден элемент {elem}')
    else:
        print(f'Элемент {elem} не найден')