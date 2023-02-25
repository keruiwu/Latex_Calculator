import sympy

def Unary_quadratic(L):
    eq_String = L
    Lats_List = []
    Part = ""   #Th temp name for part
    Syb = ""    #The temp variable for +, -
    eq_List = [] #List of each part in the equation 
    eq_Part_Dc = {} #Temp Dictioninary for each part
    for i in eq_String:
        if i == '+' or i == '-':
            index = 0
            
            for j in range(len(Part)):
                if Part[j].isalpha():
                    index = j
            print(j)
            eq_Part_Dc["const"], eq_Part_Dc["power"]= Part[0:(j-1)], Part[j:len(Part-1)]
            eq_Part_Dc["syb"] = Syb
            print(eq_Part_Dc)
            Syb = i
            Part = ""
            eq_List.append(eq_Part_Dc)
        else:
            Part+=i

Unary_quadratic("6x+y")