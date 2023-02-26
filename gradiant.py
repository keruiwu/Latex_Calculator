import derivative as d

def gradiant(Line):
    Var = set()
    for i in Line:
        if i.isalpha():
            Var.add(i)
    if len(Var)==2:
        dx = d.derivative('((d('+ Line +'))/(dx))')
        dy = d.derivative('((d('+ Line +'))/(dy))')
        return "<"+dx+", "+dy+">"
    elif len(Var)==3:
        dx = d.derivative('((d('+ Line +'))/(dx))')
        dy = d.derivative('((d('+ Line +'))/(dy))')
        dz = d.derivative('((d('+ Line +'))/(dz))')
        return "<"+dx+", "+dy+", "+dz+">"
if __name__ == '__main__':
    print(gradiant("x**2-x-6+y**(3)+z"))