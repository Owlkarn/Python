import view, model

def init_data():
    a = view.input_data('A')
    b = view.input_data('B')
    oper = view.input_operation()
    model.init_a(a)
    model.init_b(b)
    model.init_oper(oper)
    
def get_values():
    a = model.get_a()
    b = model.get_b()
    view.out_data(a)
    view.out_data(b)
    
def print_result():
    oper = model.get_oper()
    if oper == '+':
        result = model.sum_data() 
    elif oper == '-':
        result = model.minus_data()
    elif oper == '*':
        result = model.mult_data()
    elif oper == '/':
        result = model.div_data()
    view.out_result(result)