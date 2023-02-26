from sympy import *
from integral import integral

def seperable_variable(or_eq):
    RHS = or_eq.split('=')[1]
    if '/' in RHS:
        numerator = RHS.split('/')[0][1:]
        denomenator = RHS.split('/')[1][:-1]
        if 'x' in numerator:
            int_x = "\int " + numerator + "dx"
            int_y = "\int " + denomenator + "dy"
        else:
            int_x = '\int (1/' + denomenator + ')dx'
            int_y = '\int (1/' + numerator + ')dy'
        result_step1 = int_x + '=' + int_y
        print(int_x, int_y)
        result_step2 = integral(int_x) + '=' + integral(int_y)[:-2]
        return [result_step1, result_step2]
    else:
        if RHS.find("x*y") != -1:
            index = RHS.find("x*y")+1
            int_x = '\int (' + RHS[0:index] + ')dx'
            int_y = '\int (1/' + RHS[index+1:] + ')dy'
            result_step1 = int_x + '=' + int_y
            result_step2 = integral(int_x) + '=' + integral(int_y)[:-2]
            return [result_step1, result_step2]
        elif RHS.find("y*x") != -1:
            index = RHS.find("y*x")+1
            int_y = '\int (1/' + RHS[0:index] + ')dy'
            int_x = '\int (' + RHS[index+1:] + ')dx'
            result_step1 = int_x + '=' + int_y
            result_step2 = integral(int_x) + '=' + integral(int_y)[:-2]
            return [result_step1, result_step2]
        elif RHS.find(")*(") != -1:
            index = RHS.find(")*(")+1
            if 'x' in RHS[0:index]:
                int_x = '\int (' + RHS[0:index] + ')dx'
                int_y = '\int (1/' + RHS[index+1:] + ')dy'
                result_step1 = int_x + '=' + int_y
                result_step2 = integral(int_x) + '=' + integral(int_y)[:-2]
                return [result_step1, result_step2]
            else:
                int_y = '\int (1/' + RHS[0:index] + ')dy'
                int_x = '\int (' + RHS[index+1:] + ')dx'
                result_step1 = int_x + '=' + int_y
                result_step2 = integral(int_x) + '=' + integral(int_y)[:-2]
                return [result_step1, result_step2]
        elif RHS.find(")*") != -1 and RHS[RHS.find(")*")+2].isdigit():
            index = RHS.find(")*")+1
            if 'x' in RHS[0:index]:
                int_x = '\int (' + RHS[0:index] + ')dx'
                int_y = '\int (1/' + RHS[index+1:] + ')dy'
                result_step1 = int_x + '=' + int_y
                result_step2 = integral(int_x) + '=' + integral(int_y)[:-2]
                return [result_step1, result_step2]
            else:
                int_y = '\int (1/' + RHS[0:index] + ')dy'
                int_x = '\int (' + RHS[index+1:] + ')dx'
                result_step1 = int_x + '=' + int_y
                result_step2 = integral(int_x) + '=' + integral(int_y)[:-2]
                return [result_step1, result_step2]



if __name__ == "__main__":
    test = "(dy/dx)=((2*y + cos(y))/(6*x**2))"
    test1 = "(dy/dx)=2*(1 + x)*(4 + y**2)"
    test2 = "(dy/dx)=2*y*x**2"
    test3 = "(dy/dx)=2*(1 + x)*4*(4 + y**2)"
    seperable_variable(test)
    print(seperable_variable(test1))
    print(seperable_variable(test2))
    print(seperable_variable(test3))