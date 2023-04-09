#coding=utf8
def graficar(x: list, y: list):
    import matplotlib.pyplot as plt
    import numpy as np
    x,y = np.array(x), np.array(y)
    plt.figure()
    plt.title('Serie histórica de TPD')
    plt.plot(x, y, marker='.', color='k', ls='', label='Datos históricos')

    a, b = ajuste_lineal(x,y)[1], ajuste_lineal(x,y)[0]
    plt.plot(x, a+b*x, marker='.', color='r', ls='--', label=f'Ajuste lineal: y={a}+{b}X')

    c, d = ajuste_log(x,y)
    plt.plot(x, c*(d**x), marker='.', color='b', ls='--', label=f'Ajuste log: y={c}*{d}^X')

    plt.grid(ls="--")
    plt.xlabel('Factor de equivalencia')
    plt.ylabel('TPDA')
    plt.legend()
    plt.show()


def ajuste_lineal(x:list, y:list):
    import numpy as np
    ajuste = np.polyfit(x,y,1)
    a = round(ajuste[0],2)
    b = round(ajuste[1],2)
    return [a,b]


def ajuste_log(x:list, y:list):
    import numpy as np
    ajuste = np.polyfit(x,np.log10(y),1)
    al, bl = ajuste[1], ajuste[0]
    al, bl = round(10**al,3), round(10**bl, 3)
    return [al, bl]


def TPD(n:int, a:float, b:float):
    n = float(input('Ingrese el año de inicio de operacion del proyecto: '))
    return a*(b**n)

def Tacum(n:int, a:float, b:float):
    import numpy as np
    n = float(input('Ingrese el año del periodo de diseño del proyecto: '))
    return a*((b**n-1)/(np.log(b)))

def A(n:int):
    #Factor de distribución direccional
    if n == 0 or n==1:
        if n==0:
            return 0.5
        else:
            return 0.55

def B(c:int):
    #Factor carril
    if c == 1:
        return 1
    elif c == 2:
        return 0.9
    elif c == 3:
        return 0.7
    elif c == 4:
        return 0.4


def FC():
    pass





##------------------------------------------------------------------------------------##

x = [0, 1, 2, 3, 4, 5]
y = [2322, 2327, 2368, 2472, 2682, 2789]

print(B(3))


