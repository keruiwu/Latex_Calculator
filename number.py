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
    Lat_List["Title"].append("".join(str(item) for item in Binary))
    Lat_List["Subtitle"].append("Final result is this!")
    return Lat_List

def Binary_convertD(S):
    S=S[::-1]
    Latx = ""
    for i in range(len(S)):
        if i == len(S)-1:
             Latx += "2^{" + str(i) + "}"
        elif S[i] == '1':
            Latx += "2^{" + str(i) + "}" + " + "
    Latx += ' = ' + str(int(S[::-1],2))
    return Latx


if __name__ == '__main__':
    print(decimal_convertB(99))
    print(Binary_convertD("1000110101010"))