from sympy import *
from parsing import ToClose


def integral(eq):
    # \int_{a}^{b} (x ** 2 + (1/x))
    eq_end = len(eq) - 1 - eq[::-1].find(')')
    var = eq[eq_end + 2:]
    if var == 'lambda':
        var = 'lamda'
    var = symbols(var)
    if eq[4] != '_':  # 不定积分
        equation = eq[6:eq_end]
        equation = simplify(equation.replace('lambda', 'lamda'))
        return latex(integrate(equation, var)) + '+C'
    else:  # 定积分
        direct = ToClose(eq[6:])
        b = direct['result']  # 上限
        b_end = direct['index']
        direct = ToClose(eq[5 + b_end+4:])
        a = direct['result']  # 下限
        equation = eq[5 + b_end + 4 + direct['index'] + 3:eq_end]
        equation = simplify(equation.replace('lambda', 'lamda'))
        return integrate(equation, (var, a, b))


if __name__ == '__main__':
    eq = '\int (x ** 2 + (1/x))dx'  # equation must be surrounded by parenthesis
    eq_2 = '\int_{b}^{a} (x ** 2 + (1/x))dx'
    print(integral(eq))