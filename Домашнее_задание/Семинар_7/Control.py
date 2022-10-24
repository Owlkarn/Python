import View,Model

def start():
    equation = View.InputData()
    Model.set_equation(equation)
    equation_list = Model.separate_string(equation)
    Model.set_equation_list(equation_list)
    Model.search_operator()
    result = Model.get_result()
    View.OutputResult(result)
    View.print_window(result)
    