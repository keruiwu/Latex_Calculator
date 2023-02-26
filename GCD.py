import sympy
def gcd(first, second, L=[]):
    if (first%second) == 0:
        L.append("{}/{} remains 0, so the Great Common factor is".format(first,second))
        L.append(str(second))
        return L
    else:
        L.append("{}/{} = {}, remains {}".format(first,second, first//second, first%second))
        return gcd(second, first%second,L)
    

if __name__ == '__main__':
    print(gcd(25,36))