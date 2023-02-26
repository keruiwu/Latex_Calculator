from sympy import *

def To_Close(temp):
    """

    :param temp: sentence start with the character just after the beginning of {
    :return: {index: index of close ')', result: content inside the curly }
    """
    wait_list = 1
    result = ''
    for i in range(len(temp)):
        if temp[i] == '(':
            wait_list += 1
        elif temp[i] == ')':
            wait_list -= 1
        if wait_list == 0:
            return {
                'index': i,
                'result': result
            }
        result += temp[i]
    return {
        'index': -1,
        'result': 'invalid Latex'
    }


def derivative(eq):  # $$\frac{d\frac{1}{x}}{dx}$$
    # eq = 'd(sin(lambda) ** 2)/dlambda'
    left_temp = To_Close(eq[2:])
    right = eq[3+left_temp['index']:].strip(')')
    eq_start = eq.find('d')+2
    temp = To_Close(eq[eq_start:])
    eq_end = eq_start + temp['index']
    equation = eq[eq_start:eq_end]
    var = right[3:]
    if var == 'lambda':
        var = 'lamda'
    equation = equation.replace('lambda', 'lamda')
    equation = simplify(equation)
    var = symbols(var)
    return latex(diff(equation, var))


if __name__ == '__main__':#$$\frac{d\frac{1}{x}}{dx}$$
    test = "$$\\frac{d\\frac{1}{x}}{dx}$$"
    print(derivative(parsing(test)))