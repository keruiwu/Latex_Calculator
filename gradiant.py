import derivative as d

def gradiant(Line):
    Var = set()
    for i in Line:
        if i.isalpha():
            Var.add(i)
    print(Var)
    if len(Var)==2:
        dx = d.derivative('d('+ Line +')/dx')
        dy = d.derivative('d('+ Line +')/dy')
        return "<"+dx+">, <"+dy+">"
    elif len(Var)==3:
        dx = d.derivative('d('+ Line +')/dx')
        dy = d.derivative('d('+ Line +')/dy')
        dz = d.derivative('d('+ Line +')/dz')
        return "<"+dx+">, <"+dy+">, <"+dz+">"

print(gradiant("2*x**2+3*y**2+2*z**2"))