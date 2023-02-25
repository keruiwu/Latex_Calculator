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
        'result': '(' + str(a) + '/' + str(direct['result']) + ')'
    }


def power_latex(la, power_index):
    direct = ToClose(la[power_index:])
    return {
        'index': power_index + direct['index'],
        'result': la[power_index-3:power_index-2] + '**(' + str(direct['result']) + ')'
    }


def parsing(la):
    frac_index = la.find('\\frac')
    while frac_index != -1:
        frac_result = frac(la, frac_index+6)  # 6 means "\\frac{"
        la = la[:frac_index] + frac_result['result'] + la[frac_result['index']-1:]
        frac_index = la.find('\\frac')
    power_index = la.find('^')
    while power_index != -1:
        power_result = power_latex(la, power_index+2)
        print(power_result['result'])
        la = la[:power_index-1] + power_result['result'] + la[power_result['index']+1:]
        power_index = la.find('^')
    cdot_index = la.find('\\cdot')
    while cdot_index != -1:
        la = la[:cdot_index] + '*' + la[cdot_index+5:]
        cdot_index = la.find('\\cdot')
    times_index = la.find('\\times')
    while times_index != -1:
        la = la[:times_index] + '*' + la[times_index+6:]
        times_index = la.find('\\times')
    sin_index = la.find('[')
    while sin_index != -1:
        la = la[:sin_index] + '(' + la[sin_index+1:]
    sin_index = la.find(']')
    while sin_index != -1:
        la = la[:sin_index] + ')' + la[sin_index + 1:]

    return la


if __name__ == '__main__':
    print(parsing('a + \\frac{a^{2 * a}}{b} + c \\times d'))