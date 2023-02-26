from sympy import *
from integral import integral

def seperable_variable(or_eq):
    RHS = or_eq.split('=')[1]
    if '/' in RHS:
        numerator = RHS.split('/')[0]
        denomenator = RHS.split('/')[1]
        if 'x' in numerator:
            int_x = "\int " + numerator + "dx"
            int_y = "\int " + denomenator + "dy"
        else:
            int_x = '\int ' + denomenator + 'dx'
            int_y = '\int ' + numerator + 'dy'
        result_step1 = int_x + '=' + int_y
        result_step2 = integral(int_x) + '=' + integral(int_y)[:-2]
        return [result_step1, result_step2]
    else:
        if RHS.find("x*y") != -1:
            index = RHS.find("x*y")+1
            if 'x'

if __name__ == "__main__":
    test = "(dy/dx)=(6*x**2)/(2*y + cos(y))"
    test1 = "(dy/dx)=2*(1 + x)*(4 + y**2)"
    test2 = "(dy/dx)=2*x*y**2"
    print(seperable_variable(test))