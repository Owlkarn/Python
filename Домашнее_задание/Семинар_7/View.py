import tkinter as tk

def InputData(string: str):
    equation=input('Введите выражение: ')
    return equation

def OutputResult(result):
    print(f'Результат операции = {result}')

def division_by_zero():
    print('Деление на ноль!!')

def print_window(result):
    win = tk.Tk()
    win.geometry('300x300+600+600')
    my_label = tk.Label(win, text=result)
    my_label.pack()
    win.mainloop()