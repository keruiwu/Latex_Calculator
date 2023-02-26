import sympy
def decimal_convertB(I):
    Num = I
    remainder = 0
    div = 0
    Binary = []
    Lat_List = {}
    Lat_List["Title"] = []
    Lat_List["Subtitle"] = []
    while(Num!= 1):
        if Num == I:
            Lat_List["Title"].append("Step to convert decimal to Binary String")
            Lat_List["Subtitle"].append("We can do it by divide decimal by 2 until the divisor is 1")
        div  = Num//2
        remainder = Num%2
        Lat_List["Title"].append("{} / 2 = {}".format(Num,div))
        Lat_List["Subtitle"].append("Write the remainder {} to the front of our binary string".format(remainder,remainder))  
        Num = div 
        Binary.append(remainder)
    Lat_List["Title"].append("1/2 remains 1")
    Lat_List["Subtitle"].append("Write 1 to the front of the bianry string and then reverse it")
    Binary.append(1)
    Binary.reverse()
    Lat_List["Title"].append("The binary string will be ")
    Lat_List["Subtitle"].append("".join(str(item) for item in Binary))
    return Lat_List

def Binary_convertD(S):
    S=S[::-1]
    Latx = ""
    for i in range(len(S)):
        if S[i] == 1:
            Latx+="2^{}".format(i)+" + "
        if i == len(S)-1:
             Latx+="2^{}".format(i)
    Latx_List = []
    Latx_List.append(Latx)
    Latx_List.append(str(int(S[::-1],2)))
    return Latx_List
print(decimal_convertB(99))  
print(Binary_convertD("1000"))