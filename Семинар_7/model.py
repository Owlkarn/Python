a = 0
b = 0
oper = ''

def init_a(value):
    global a
    a = value

def init_b(value):
    global b
    b = value
    
def init_oper(value):
    global oper
    oper = value
    
def get_a():
    global a
    return a

def get_b():
    global b
    return b

def get_oper():
    global oper
    return oper

def sum_data():
    global a
    global b
    return a+b

def minus_data():
    global a
    global b
    return a-b

def mult_data():
    global a
    global b
    return a*b

def div_data():
    global a
    global b
    return int(a/b)