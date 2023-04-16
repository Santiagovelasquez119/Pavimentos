#coding=utf8
import numpy as np
def graficar(x: list, y: list):
    import matplotlib.pyplot as plt
    import numpy as np
    x,y = np.array(x), np.array(y)
    plt.figure()
    plt.title('Serie histórica de TPD')
    plt.plot(x, y, marker='.', color='k', ls='', label='Datos históricos')

    a, b = ajuste_lineal(x,y)[1], ajuste_lineal(x,y)[0]
    plt.plot(x, a+b*x, marker='.', color='r', ls='-', label=f'Ajuste lineal: y={a}+{b}X')

    c, d = ajuste_log(x,y)
    plt.plot(x, c*(d**x), marker='.', color='b', ls='-', label=f'Ajuste log: y={c}*{d}^X')

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


def TPD(a:float, b:float):
    n = float(input('Ingrese el año de inicio de operacion del proyecto: '))
    return a*(b**n)

def Tacum(a:float, b:float):
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


def FCC():
    totalcamion = int(input('Ingrese el total de camiones: '))
    c2p = int(input('Ingrese la fracción correspondiente a la categoría C2P: '))/totalcamion
    c2g = int(input('Ingrese la fracción correspondiente a la categoría C2G: '))/totalcamion
    c3c4 = int(input('Ingrese la fracción correspondiente a la categoría C3-C4: '))/totalcamion
    c5 = int(input('Ingrese la fracción correspondiente a la categoría C5: '))/totalcamion
    mc5 = int(input('Ingrese la fracción correspondiente a la categoría >C5: '))/totalcamion
    return (c2p*1.11+c2g*2.34+c3c4*5.62+c5*7.44+mc5*7.09)


def FC(FCC: float):
    cam = float(input('Ingrese el procentaje de camiones: '))/100
    bus = float(input('Ingrese el procentaje de buses: '))/100
    return (FCC*cam+0.79*bus)/(cam+bus)

def W18(A: float, B: float, FC: float, TPD: float, Tacum: float):
    return A*B*FC*TPD*365*Tacum

def prueba(x:list, y:list):
    a,b = ajuste_lineal(x, y)
    print(f'a={a} b={b}')
    c,d = ajuste_log(x, y)
    print(f'c={c} d={d}')
    tpd = TPD(c, d)
    print(f'tpd={tpd}')
    tacum = Tacum(c, d)
    print(f'tacum={tacum}')
    fcc = FCC()
    print(f'fcc={fcc}')
    w18 = W18(A(1), B(3), FC(fcc), tpd, tacum)
    if w18 > 5*(10**6):
        print('\nNivel de tránsito 3 Base granular tipo A')
    elif 5*(10 ** 5) < w18 < 5*(10 ** 6):
        print('\nNivel de tránsito 2 Base granular tipo B')
    else:
        print('\nNivel de tránsito 2 Base granular tipo B')
    return f'Numero de ejes equivalentes {w18}'




##------------------------------------------------------------------------------------##

x = [0, 1, 2, 3, 4, 5, 6, 7]
y = [4644, 8476, 15918, 27569, 17799, 21020, 18461, 20797]

print(0.55*0.7*4950*3.43*365*(((1.040**15)-1)/np.log(1.040)))
print()

graficar(x,y)

print(prueba(x,y))


#print(prueba(x,y))

