n = float(input('Введите число: '))

if n*10%10 != 0:
    print(int(n*10%10))
else:
    print("Введено целое число")
    
# if n == int(n)