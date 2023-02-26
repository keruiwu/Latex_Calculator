import sympy
def decimal_convertB(I):
    Num = I
    remainder = 0
    div = 0
    Binary = []
    Lat_List = []
    Lat_List.append("Step to convert decimal to Binary String")
    while(Num!= 1):
        if Num == I:
            Lat_List.append("We can do it by divide decimal by 2 until the divisor is 1")
        div  = Num//2
        remainder = Num%2
        Lat_List.append("{} / 2 = {}, The remainder is {}, We write {} to the front of our binary string".format(Num,div,remainder,remainder))  
        Num = div 
        Binary.append(remainder)
    Lat_List.append("Finally, the divisor is 1, 1/2 remains 1, We write 1 to the front of the bianry string and then reverse it")
    Binary.append(1)
    Binary.reverse()
    Lat_List.append("The binary string will be ")
    Lat_List.append("".join(str(item) for item in Binary))
    return Lat_List

def Binary_convertD(S):
    return str(int(S,2))
print(decimal_convertB(99))  
print(Binary_convertD("1000"))