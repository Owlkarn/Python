def Pop_list(list, operator):
    list.pop(list.index(operator) + 1)
    list.pop(list.index(operator))
    
read_data = input('Введите выражение: ')
read_data_list = []
i=0
number = ''
plus = '+'
minus = '-'
multiply = '*'
divide = '/'

while len(read_data) > i:
    if read_data[i].isdigit():
        number += read_data[i]
    else:
        read_data_list.append(number)
        number = ''
        read_data_list.append(read_data[i])
    i+=1
read_data_list.append(number)

while len(read_data_list) != 1:
    if read_data_list.count(multiply) != 0:
        read_data_list[read_data_list.index(multiply) - 1] = int(read_data_list[read_data_list.index(multiply) - 1]) * int(read_data_list[read_data_list.index(multiply) + 1])
        Pop_list(read_data_list, multiply)
    elif read_data_list.count(divide) != 0:
        read_data_list[read_data_list.index(divide) - 1] = int(read_data_list[read_data_list.index(divide) - 1]) / int(read_data_list[read_data_list.index(divide) + 1])
        Pop_list(read_data_list, divide)
    elif read_data_list.count(minus) != 0:
        read_data_list[read_data_list.index(minus) - 1] = int(read_data_list[read_data_list.index(minus) - 1]) - int(read_data_list[read_data_list.index(minus) + 1])
        Pop_list(read_data_list, minus)
    elif read_data_list.count(plus) != 0:
        read_data_list[read_data_list.index(plus) - 1] = int(read_data_list[read_data_list.index(plus) - 1]) + int(read_data_list[read_data_list.index(plus) + 1])
        Pop_list(read_data_list, plus)

print(int(read_data_list[0]))