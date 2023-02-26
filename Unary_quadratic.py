import sympy
import parsing
def Unary_quadratic(L):
    eq_String = L.replace(" ", "")
    Lats_List = []
    Part = ""   #Th temp name for part
    Syb = ""    #The temp variable for +, -
    eq_DC = {} #List of each part in the equation 
    eq_Part_Dc = {} #Temp Dictioninary for each part
    for i in range(len(eq_String)):
        if i >= 1 and eq_String[i] == '-' and eq_String[i-1]=="(":
            Part+=eq_String[i]
        elif (eq_String[i] == '+' or eq_String[i] == '-') and i!=0 :
            index = 0
            var = ''
            for j in range(len(Part)):
                if Part[j].isalpha():
                    index = j
                    var = Part[j]

            if index==0:
                eq_Part_Dc["const"] = '1'
            else:
                eq_Part_Dc["const"] = Part[0:index-1] 
                if Part[0]=="(" and Part[index-2]== ")":
                    eq_Part_Dc["const"] = Part[1:index-2]
            eq_Part_Dc["power"] = Part[index+1:len(Part)]
            eq_Part_Dc["syb"] = Syb
            eq_Part_Dc["var"] = var

            if eq_Part_Dc["syb"]=='' and eq_Part_Dc["power"]!=''and eq_Part_Dc['var']!='':
                eq_DC["1st"] = eq_Part_Dc
            elif eq_Part_Dc["syb"]!=''and eq_Part_Dc["power"]==''and eq_Part_Dc['var']!='':
                eq_DC["2st"] = eq_Part_Dc
            elif eq_Part_Dc["var"] == '' :
                if Part[0]=='(' and Part[len(Part)-1]==')':
                    eq_Part_Dc["const"] = Part[1:len(Part)-1]
                else:
                    eq_Part_Dc["const"] = Part
                eq_DC["C"] = eq_Part_Dc

            Syb = eq_String[i]
            Part = ""
            eq_Part_Dc = {}
        
        elif i == len(eq_String)-1:
            Part+=eq_String[i]
            index = 0
            var = ''
            for j in range(len(Part)):
                if Part[j].isalpha():
                    index = j
                    var = Part[j]
            if index==0:
                eq_Part_Dc["const"] = '1'
            else:
                eq_Part_Dc["const"] = Part[0:index-1]
                if Part[0]=="(" and Part[index-2]==")":
                    eq_Part_Dc["const"] = Part[1:index-2]
            eq_Part_Dc["power"] = Part[index+1:len(Part)]
            eq_Part_Dc["syb"] = Syb
            eq_Part_Dc["var"] = var

            if eq_Part_Dc["syb"]=='' and eq_Part_Dc["power"]!='' and eq_Part_Dc['var']!='':
                eq_DC["1st"] = eq_Part_Dc
            elif eq_Part_Dc["syb"]!=''and eq_Part_Dc["power"]==''and eq_Part_Dc['var']!='':
                eq_DC["2st"] = eq_Part_Dc
            elif eq_Part_Dc["var"] == '':
                if Part[0]=='(' and Part[len(Part)-1]==')':
                    eq_Part_Dc["const"] = Part[1:len(Part)-1]
                else:
                    eq_Part_Dc["const"] = Part
                eq_DC["C"] = eq_Part_Dc

        else:
            Part+=eq_String[i]
    print(eq_DC)
    if len(eq_DC)==1:
        Lats_List.append(sympy.latex(sympy.parse_expr(eq_DC["1st"]["var"]+ "**2")) + "= 0")
        Lats_List.append(eq_DC["1st"]["var"]+ " = 0")

    elif len(eq_DC)==2:
        if "C" in eq_DC:
            if eq_DC["C"]["syb"]=="-":
                if(eq_DC["1st"]["const"])=='1':
                    Lats_List.append(sympy.latex(sympy.parse_expr(eq_DC["1st"]["var"] + "**2"))+" = " + sympy.latex(sympy.parse_expr(eq_DC["C"]["const"])))

                else:
                    Lats_List.append(sympy.latex(sympy.parse_expr(eq_DC["1st"]["const"] +"*"+ eq_DC["1st"]["var"] + "**2"))+ " = " + sympy.latex(sympy.parse_expr(eq_DC["C"]["const"])))
                    tmp = "("+eq_DC["C"]["const"]+")/("+ eq_DC["1st"]["const"]+")"
                    tmp = sympy.simplify(tmp)                       
                    Lats_List.append(sympy.latex(sympy.parse_expr(eq_DC["1st"]["var"] + "**2"))+" = " + sympy.latex(tmp))
                #Lats_List.append()
                result = sympy.solve(eq_DC["1st"]["const"] + "*"+ eq_DC["1st"]["var"] + "**2 - " + eq_DC["C"]["const"],eq_DC["1st"]["var"])
                Lats_List.append(eq_DC["1st"]["var"] + " = " + sympy.latex(result[0])+" or "+sympy.latex(result[1]))

            elif eq_DC["C"]["syb"]=="+":
                if(eq_DC["1st"]["const"])=='1':
                    Lats_List.append(sympy.latex(sympy.parse_expr(eq_DC["1st"]["var"] + "**2"))+" = " + '-' + sympy.latex(sympy.parse_expr(eq_DC["C"]["const"])))
                else:
                    Lats_List.append(sympy.latex(sympy.parse_expr(eq_DC["1st"]["const"] +"*"+ eq_DC["1st"]["var"] + "**2")) + " = " + '-' + sympy.latex(sympy.parse_expr(eq_DC["C"]["const"])))
                    tmp = "(-"+eq_DC["C"]["const"]+")/("+ eq_DC["1st"]["const"]+")"  
                    tmp = sympy.simplify(tmp)                       
                    Lats_List.append(sympy.latex(sympy.parse_expr(eq_DC["1st"]["var"] + "**2"))+" = " + sympy.latex(tmp))

                result = sympy.solve(eq_DC["1st"]["const"] + "*"+ eq_DC["1st"]["var"] + "**2 + " + eq_DC["C"]["const"],eq_DC["1st"]["var"])
                Lats_List.append(eq_DC["1st"]["var"] + " = " + sympy.latex(result[0])+" or "+sympy.latex(result[1]))
        elif "2st" in eq_DC:
            Lats_List.append(sympy.latex(sympy.factor(eq_DC["1st"]["const"] +"*" + eq_DC["1st"]["var"] + "**2" + eq_DC["2st"]["syb"]+eq_DC["2st"]["const"]+"*"+eq_DC["2st"]["var"])))
            result = sympy.solve(eq_DC["1st"]["const"] +"*" + eq_DC["1st"]["var"] + "**2" + eq_DC["2st"]["syb"]+eq_DC["2st"]["const"]+"*"+eq_DC["2st"]["var"], eq_DC["1st"]["var"])
            Lats_List.append(eq_DC["1st"]["var"]+" = "+sympy.latex(result[0])+" or "+sympy.latex(result[1]))

    elif len(eq_DC)==3:
        a = eq_DC["1st"]["const"]
        if eq_DC["2st"]["syb"]=='+':
            b = eq_DC["2st"]["const"]
        else:
            b = "-"+eq_DC["2st"]["const"]
        
        if eq_DC["C"]["syb"]=='+':
            c = eq_DC["C"]["const"]
        else:
            c = '-'+eq_DC["C"]["const"]
        
        Lats_List.append("\\delta = "+sympy.latex(sympy.parse_expr("b**2 - 4 * a * c")))
        Lats_List.append("x = \\frac{- b \\pm \\sqrt{- 4 a c + b^{2}}}{2 a}")
        Lats_List.append("x = \\frac{- "+sympy.latex(sympy.parse_expr(b))+ "\\pm \\sqrt{- 4 "+"\\times"+sympy.latex(sympy.parse_expr(a))+" "+ "\\times"+ sympy.latex(sympy.parse_expr(c)) + " + " + sympy.latex(sympy.parse_expr(b)) + "^{2}}}{2 " + "\\times"+sympy.latex(sympy.parse_expr(a))+"}")
        result = sympy.solve(eq_DC["1st"]["const"]+"*"+eq_DC["1st"]["var"]+"**2"+eq_DC["2st"]["syb"]+eq_DC["2st"]["const"]+"*"+eq_DC["2st"]["var"]+eq_DC["C"]["syb"]+eq_DC["C"]["const"],eq_DC["1st"]["var"])
        if len(result)==1:
            Lats_List.append(eq_DC["1st"]["var"]+" = "+sympy.latex(result[0]))
        else:
            Lats_List.append(eq_DC["1st"]["var"]+" = "+sympy.latex(result[0])+" or "+sympy.latex(result[1]))
    
    return Lats_List


if __name__ == '__main__':
    print(Unary_quadratic("(-5/4)*x**          2+2* x+ 1 "))

