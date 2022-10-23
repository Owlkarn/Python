# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbcccccccccd => 7a6b9c1d или 11a3b7c1d => aaaaaaaaaaabbbcccccccd

pathRead = 'Text_4.txt'
pathWrite = 'Text_4_1.txt'

with open(pathRead, "r", encoding='UTF-8') as data:
    read_data = data.readline()
with open(pathWrite, 'w', encoding='UTF-8') as data:
    data.write('')

if read_data[0].isdigit():
    number = []
    literal = []
    temp = ''
    l = ''
    i = 0
    
    while len(read_data) > 0:
        while read_data[i].isdigit():
            temp += read_data[i]
            i += 1
        number.append(temp)
        temp = ''
        read_data = read_data[i:]
        i = 0
        while not read_data[i].isdigit():
            temp += read_data[i]
            i += 1
            if i == len(read_data):
                break
        literal.append(temp)
        temp = ''
        read_data = read_data[i:]
        i = 0
    for j in range(len(number)):
        with open(pathWrite, 'a', encoding='UTF-8') as data:
            data.write(int(number[j]) * literal[j])
else:
    number = []
    literal = []
    while len(read_data) > 0:
        literal.append(read_data[0])
        number.append(read_data.count(read_data[0]))
        read_data = read_data.replace(read_data[0], '')
    for i in range(len(number)):
        with open(pathWrite, 'a', encoding='UTF-8') as data:
            data.write(str(number[i]) + literal[i])        

print(number)
print(literal)
    

