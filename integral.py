from sympy import *

def ToClose(temp):
    """

    :param temp: sentence start with the character just after the beginning of {
    :return: {index: index of close '}', result: content inside the curly }
    """
    wait_list = 1
    result = ''
    for i in range(len(temp)):
        if temp[i] == '{':
            wait_list += 1
        elif temp[i] == '}':
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
        return latex(integrate(equation, (var, a, b)))


if __name__ == '__main__':
    eqs = ['\int (x ** 2 + (1/x))dx', '\int_{b}^{a} (x ** 2 + (1/x))dx', "\int (1/(2*y + cos(y)))dy", "\int (1/(6*x**2))dx", "\int (3*x**2+4*x-5)dx", 
           "\int ((x+1)*e**(2*x))dx"]
    for e in eqs:
        print(integral(e))
        print()