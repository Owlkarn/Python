import View,Model

def start():
    i=0
    number = ''
    equation_list = []
    equation = View.InputData()
    operation = ['*', '/', '-', '+']
    
    while len(equation) > i:
        if equation[i].isdigit():
            number += equation[i]
        else:
            equation_list.append(number)
            number = ''
            equation_list.append(equation[i])
        i+=1
    equation_list.append(number)
    
    while len(equation_list) > 1:
        if operation[0].count(equation_list) != 0 or operation[1].count(equation_list) != 0:
            
    a = View.InputData('первое')
    Model.set_first(a)
    while True:
        oper = View.InputOperator()
        if oper == '=': break
        b = View.InputData('второе')
        Model.set_second(b)
        Model.set_result(oper)
        result = Model.get_result()
        if result == None:
            View.division_by_zero()
            break
        first = Model.get_first()
        second = Model.get_second()
        View.OutputResult(first, second, oper, result)
        View.print_window(result)
        Model.set_first(result)