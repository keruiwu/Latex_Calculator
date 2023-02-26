import sympy
def Brick(S):
    return sympy.latex(sympy.Rational(sympy.parse_expr(S).evalf()))


if __name__ == '__main__':
    print(Brick("((5)/(4))*((5)/(4))"))