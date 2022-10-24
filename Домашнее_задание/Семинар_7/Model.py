first = 0
second = 0
result = 0
equation_list = []
equation = ''
operation = ['*', '/', '-', '+']

listOperator = {'*': lambda x,y: int(x) * int(y),
                '/': lambda x,y: int(x) / int(y),
                '+': lambda x,y: int(x) + int(y),
                '-': lambda x,y: int(x) - int(y)}

def get_result():
    global equation_list
    return int(equation_list[0])

def set_equation(eq: str):
    global equation
    equation = eq
    
def set_equation_list(eq_list: list):
    global equation_list
    equation_list = eq_list

def pop_list(list, operator):
    list.pop(list.index(operator) + 1)
    list.pop(list.index(operator))
    
def separate_string(equation):
    global equation_list
    i = 0
    number = ''
    while len(equation) > i:
        if equation[i].isdigit():
            number += equation[i]
        else:
            equation_list.append(number)
            number = ''
            equation_list.append(equation[i])
        i+=1
    equation_list.append(number)
    return equation_list

def search_operator():
    global equation_list
    i = 0
    while len(equation_list) > 1:
        if equation_list.count(operation[i]) == 0:
            i += 1
        else:
            equation_list[equation_list.index(operation[i]) - 1] = listOperator.get(operation[i])(equation_list[equation_list.index(operation[i]) - 1], equation_list[equation_list.index(operation[i]) + 1])
            pop_list(equation_list, operation[i])