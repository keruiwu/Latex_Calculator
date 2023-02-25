from sympy import *


def derivative(eq):
    # eq = 'd(sin(lambda) ** 2)/dlambda'
    eq_start = eq.find('(')+1
    eq_reverse = eq[::-1]
    eq_end = len(eq) - 1 - eq_reverse.find(')')
    equation = eq[eq_start:eq_end]
    print(equation)
    var = eq[eq_end+3:]
    if var == 'lambda':
        var = 'lamda'
    equation = equation.replace('lambda', 'lamda')
    equation = simplify(equation)
    var = symbols(var)

    return latex(diff(simplify(equation), var))


if __name__ == '__main__':
    print(derivative('d((sin(x) ** 2) * lambda)/dx'))