# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def check(value):
    match value:
        case '1':
            print('X от 0 до +∞')
            print('Y от 0 до +∞')
        case '2':
            print('X от -∞ до 0')
            print('Y от 0 до +∞')
        case '3':
            print('X от -∞ до 0')
            print('Y от -∞ до 0')
        case '4':
            print('X от 0 до +∞')
            print('Y от -∞ до 0')
        case _:
            print('Введен неверный номер четверти')


n = input('Введите номер четверти: ')
check(n)
