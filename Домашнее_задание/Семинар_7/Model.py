first = 0
second = 0
result = 0

listOperator = {'*': lambda x,y: int(x) * int(y),
                '/': lambda x,y: int(x) / int(y),
                '+': lambda x,y: int(x) + int(y),
                '-': lambda x,y: int(x) - int(y)}


def set_first(number: int):
    global first
    first = number

def set_second(number: int):
    global second
    second = number

def set_result(oper: str):

    ### ДЕЛЕНИЕ НА НОЛЬ!!!!
    global result
    global second
    result = listOperator.get(oper)(first, second)


def get_first():
    global first
    return first

def get_second():
    global second
    return second

def get_result():
    global result
    return result

def Pop_list(list, operator):
    list.pop(list.index(operator) + 1)
    list.pop(list.index(operator))
    
def Operation_done():
    