array = []
for i in range(5):
    array.append(int(input(f'Введите {i+1} число: ')))
max = array[0]

for i in range(1, len(array)):
    if array[i] > max:
        max = array[i]

# for i in array:
#     if max < i:
#         max = i

print(max)
