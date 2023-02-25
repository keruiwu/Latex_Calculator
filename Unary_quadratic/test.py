import sympy

print(sympy.factor("x**2+x"))
print(sympy.latex("1*x**2+x"))
#sympy.solveset(sympy.Eq("x**2 - x", 0), "x", domain = sympy.S.Reals)
print(sympy.solve("sqrt(2)*x**2 - 5","x"))
print(sympy.simplify("(--5+sqrt(-5**2-4*-1*4))/(2*-1)"))