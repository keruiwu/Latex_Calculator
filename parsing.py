from differential_equation import seperable_variable as s
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


def frac(la, frac_index):
    """

    :param la: original latex string
    :param frac_index: index of the beginning of frac ()
    """
    direct = ToClose(la[frac_index:])
    a = direct['result']
    a_end = frac_index + direct['index']  # }{...}
    direct = ToClose(la[a_end+2:])
    return {
        'index': a_end + 2 + direct['index'] + 2,
        'result': '((' + str(a) + ')/(' + str(direct['result']) + '))'
    }


def power_latex(la, power_index):
    direct = ToClose(la[power_index:])
    return {
        'index': power_index + direct['index'],
        'result': la[power_index-3:power_index-2] + '**(' + str(direct['result']) + ')'
    }

def sqrt(la, sqrt_start):
    sqrt_index_end = la.find('}')
    sqrt_eq = '(' + la[sqrt_start:sqrt_index_end] + ')'
    return sqrt_eq, la, sqrt_index_end

def parsing(la):
    greek = ["\\alpha", "\\beta", "\\gamma", "\\delta", "\\varepsilon", "\\eta", "\\theta", "\\iota", "\\kappa", "\\lambda",
     "\\mu", "\\nu", "\\xi", "\\o", "\\pi", "\\rho", "\\sigma", "\\tau", "\\upsilon", "\\varphi", "\\chi", "\\psi",
     "\\omega"]
    la = la.strip('$$')
    la = la.strip('$')
    frac_index = la.find('\\frac')
    while frac_index != -1:
        frac_result = frac(la, frac_index+6)  # 6 means "\\frac{"
        la = la[:frac_index] + frac_result['result'] + la[frac_result['index']-1:]
        frac_index = la.find('\\frac')

    power_index = la.find('^')
    while power_index != -1:
        if la[power_index+1] == '{':
            power_result = power_latex(la, power_index+2)
            la = la[:power_index-1] + power_result['result'] + la[power_result['index']+1:]
        else:
            la = la[:power_index] + '**' + la[power_index+1:]
        power_index = la.find('^')

    cdot_index = la.find('\\cdot')
    while cdot_index != -1:
        la = la[:cdot_index] + '*' + la[cdot_index+5:]
        cdot_index = la.find('\\cdot')

    times_index = la.find('\\times')
    while times_index != -1:
        la = la[:times_index] + '*' + la[times_index+6:]
        times_index = la.find('\\times')

    lsqbracket_index = la.find('[')
    while lsqbracket_index != -1:
        la = la[:lsqbracket_index] + '(' + la[lsqbracket_index+1:]
        lsqbracket_index = la.find('[')

    rsqbracket_index = la.find(']')
    while rsqbracket_index != -1:
        la = la[:rsqbracket_index] + ')' + la[rsqbracket_index + 1:]
        rsqbracket_index = la.find(']')

    sin_index = la.find('\\sin')
    while sin_index != -1:
        la = la[0:sin_index] + la[sin_index+2:]
        sin_index = la.find('\\sin')
    
    tan_index = la.find('\\tan')
    while tan_index != -1:
        la = la[0:tan_index] + la[tan_index+2:]
        tan_index = la.find('\\tan')
    
    cos_index = la.find('\\cos')
    while cos_index != -1:
        la = la[0:cos_index] + la[cos_index+2:]
        cos_index = la.find('\\cos')

    ln_index = la.find('\\ln')
    while ln_index != -1:
        la = la[0:ln_index] + la[ln_index+2:]
        ln_index = la.find('\\ln')
    
    log_index = la.find('\\log')
    while log_index != -1:
        la = la[0:log_index] + la[log_index+2:]
        log_index = la.find('\\log')
    
    sqrt_index = la.find('\\sqrt')
    while sqrt_index != -1:
        sqrt_result, sqrt_half, end = sqrt(la[sqrt_index+1:], 5)
        la = la[0:sqrt_index] + la[sqrt_index+1:sqrt_index+5] + sqrt_result + sqrt_half[end+1:]
        sqrt_index = la.find('\\sqrt')
    i = 0
    while i < len(la):
        if i == len(la) - 1:
            break
        if la[i].isdigit():
            if la[i+1] == '\\' or la[i+1].isalpha() or la[i+1] == '(':  # 2x => 2 * x
                la = la[:i+1] + '*' + la[i+1:]
        elif la[i] == ')':  # (2+x)(3+y)
            if la[i+1].isalnum() or la[i+1] == '(':
                la = la[:i+1] + '*' + la[i+1:]
        elif la[i] == '\\':
            if la[i-1].isalpha():
                la = la[:i] + '*' + la[i:]
        i += 1
    for i in greek:
        la = la.replace(i, i[1:])
    return la


if __name__ == '__main__':
    # test = "f(x,y)=2x^3y^4-(4x^5y^3-6x^2)(a\delta)2(x+3)"
    # print(parsing(test))
    test = "$$\\frac{dy}{dx}=\\frac{(2*y + cos(y))}{(6*x**2)}$$"
    print(parsing(test))
    print(s(parsing(test)))