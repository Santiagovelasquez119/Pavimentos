#coding=utf8
from numpy import log
def A(W18: float, B:float, FC:float, TPD:float, b:float, n:float):
    #Factor de distribución direccional
    exp = ((b**n)-1)/log(b)
    return W18/(B*FC*TPD*365*exp)

def B(W18: float, A:float, FC:float, TPD:float, b:float, n:float):
    exp = ((b ** n) - 1) / log(b)
    return W18 / (A * FC * TPD * 365 * exp)

def FC(W18: float, A:float, B:float, TPD:float, b:float, n:float):
    exp =((b ** n) - 1) / log(b)
    return W18 / (A * B * TPD * 365 * exp)

def TPD(W18: float, A:float, B:float, FC:float, b:float, n:float):
    exp = ((b ** n) - 1) / log(b)
    return W18 / (A * B * FC * 365 * exp)


print(TPD(15226449, 0.55,0.7, 3.2765848, 1.025164328, 10))