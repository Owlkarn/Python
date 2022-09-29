a = int(input('Введите а: ')) 
b = int(input('Введите b: ')) 
if a**2 == b or b**2 == a:  # a == pow(b,2) or b == a pow(a,2)
    print('Да')
else:
    print('Нет')
