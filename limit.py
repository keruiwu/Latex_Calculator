from sympy import *
from parsing import parsing

def cal_limit(or_eq):
    index_to = or_eq.find("\\to")
    num_to_end = or_eq.find('}')
    var_to = symbols(or_eq[index_to - 2])
    num_to = -1
    if or_eq[index_to + 4].isdigit() or (or_eq[index_to + 3] == '-' and or_eq[index_to + 5].isdigit()):
        num_to_start = index_to + 3
        num_to = int(or_eq[num_to_start:num_to_end])
    elif or_eq[index_to + 5].isalpha():
        num_to = oo
    elif (or_eq[index_to + 4] == '-' and or_eq[index_to + 6].isalpha()):
        num_to = -oo

    limit_str = or_eq[num_to_end+2:-1]
    limit_exp = simplify(limit_str)
    print(limit_exp, var_to, num_to)
    result = limit(limit_exp, var_to, num_to)
    if "Limit" in str(result):
        return "Error -- Not suitable input! Please check your approches value!"
    return result
    
if __name__ == '__main__':
    # test = ["\lim_{x \to \infty} (3*x**2+7*x**3)/(x**2+5*x**4)", "\lim_{x \to -\infty} (3*x**2+7*x**3)/(x**2+5*x**4)", "\lim_{x \to 0} (3*x**2+7*x**3)/(x**2+5*x**4)", 
    #         "\lim_{x \to 10} (3*x**2+7*x**3)/(x**2+5*x**4)", "\lim_{x \to 5} (3*x**2+7*x**3)/(x**2+5*x**4)", "\lim_{x \to 3} (7*x**3)/(x**2+5*x**4+x**5+x*8)", 
    #         "\lim_{x \to \infty} ((sin (x)) / x)** cos(x)", "\lim_{x \to 0} ((sin (x)) / x)** cos(x)"]
    test = ["$$\\lim_{x \\to \\infty} \\frac{3x^2+7x^3}{x^2+5x^4}$$", "$$\\lim_{z \\to 0} \\frac{1-cos(z)}{z^2}$$"]
    
    for t in test:
        parse = parsing(t)
        print(parse)
        print()
        print(cal_limit(parse))
        print()