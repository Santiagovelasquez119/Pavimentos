# coding=utf8
import numpy as np
import math


def graficar(x: list, y: list):
    import matplotlib.pyplot as plt
    import numpy as np
    x, y = np.array(x), np.array(y)
    plt.figure()
    plt.title('Serie histórica de TPD')
    plt.plot(x, y, marker='o', color='k', ls='', label='Datos históricos')

    a, b = ajuste_lineal(x, y)[1], ajuste_lineal(x, y)[0]
    plt.plot(x, a + b * x, marker='.', color='r', ls='-', label=f'Ajuste lineal: y={a}+{b}x')

    c, d = ajuste_exp(x, y)
    plt.plot(x, c * (d ** x), marker='.', color='b', ls='-', label=f'Ajuste log: y=({c})({d}^x)')

    plt.grid(ls="--")
    plt.xlabel('Factor de equivalencia')
    plt.ylabel('TPDA')
    plt.legend()
    plt.show()


def ajuste_lineal(x: list, y: list):
    import numpy as np
    ajuste = np.polyfit(x, y, 1)
    a = ajuste[0]
    b = ajuste[1]
    return [a, b]


def ajuste_exp(x: list, y: list):
    import numpy as np
    ajuste = np.polyfit(x, np.log10(y), 1)
    al, bl = ajuste[1], ajuste[0]
    al, bl = 10 ** al, 10 ** bl
    return [al, bl]


def TPD(Ti: float, Tcrecimiento: float):
    n = float(input('Ingrese el año de inicio de operacion del proyecto: '))
    #tpd = math.ceil((Ti) * (Tcrecimiento ** n))
    tpd = (Ti) * (Tcrecimiento ** n)
    return tpd


def Tacum(a: float, b: float):
    import numpy as np
    n = float(input('Ingrese el año del periodo de diseño del proyecto: '))
    return a * ((b ** n) - 1) / (np.log(b))


def A():
    # Factor de distribución direccional
    print('Ingrese 0 para A=0.5 o ingrese 1 para A=0.55')
    n = int(input('Ingrese el valor de distribución direccional: '))
    if n == 0 or n == 1:
        if n == 0:
            return 0.5
        else:
            return 0.55


def B():
    # Factor carril
    c = int(input('Ingrese el número de carriles: '))
    if c == 1:
        return 1
    elif c == 2:
        return 0.9
    elif c == 3:
        return 0.7
    elif c == 4:
        return 0.4


def FECE():
    C2P = ((40 / 80) ** 3.25) + ((80 / 80) ** 3.25)
    C2G = ((54 / 80) ** 3.25) + ((100 / 80) ** 3.25)
    C3 = ((44 / 80) ** 3.25) + ((135 / 80) ** 3.25)
    C2S3 = ((44 / 80) ** 3.25) + ((60 / 80) ** 3.25) + ((135 / 80) ** 3.25)
    C3S3 = ((44 / 80) ** 3.25) + ((90 / 80) ** 3.25) + ((125 / 80) ** 3.25)
    Bus = ((44 / 80) ** 3.25) + ((70 / 80) ** 3.25)
    return [C2P, C2G, C3, C2S3, C3S3, Bus]


def FCC():
    totalcamion = int(input('Ingrese el total de camiones: '))
    c2p = int(input('Ingrese la fracción correspondiente a la categoría C2P: ')) / totalcamion
    c2g = int(input('Ingrese la fracción correspondiente a la categoría C2G: ')) / totalcamion
    c3c4 = int(input('Ingrese la fracción correspondiente a la categoría C3-C4: ')) / totalcamion
    c5 = int(input('Ingrese la fracción correspondiente a la categoría C5: ')) / totalcamion
    mc5 = int(input('Ingrese la fracción correspondiente a la categoría >C5: ')) / totalcamion
    return (c2p * FECE()[0] + c2g * FECE()[1] + c3c4 * FECE()[2] + c5 * FECE()[3] + mc5 * FECE()[4])


def FC(FCC: float):
    cam = float(input('Ingrese el procentaje de camiones: ')) / 100
    bus = float(input('Ingrese el procentaje de buses: ')) / 100
    return (FCC * cam + FECE()[5] * bus) / (cam + bus)


def W18(FA: float, FB: float, FC: float, TPD: float, Tacum: float):
    return FA * FB * FC * TPD * 365 * Tacum / ajuste_exp(x, y)[0]


def niveltransito(w18: float):
    if w18 > 5 * (10 ** 6):
        return 'Nivel de tránsito 3 Base granular tipo A'
    elif 5 * (10 ** 5) < w18 < 5 * (10 ** 6):
        return 'Nivel de tránsito 2 Base granular tipo B'
    else:
        return 'Nivel de tránsito 2 Base granular tipo B'


def prueba(x: list, y: list):
    a, b = ajuste_lineal(x, y)
    c, d = ajuste_exp(x, y)
    tpd = round(TPD(c, d))
    tacum = Tacum(c, d)
    fcc = FCC()
    FA = A()
    FB = B()
    fc = FC(fcc)
    w18 = W18(FA, FB, fc, tpd, tacum)

    def reporte():
        print('\n-------------------------------------')
        print('Reporte de resultados\n')
        print(f'Ajuste lineal: {a}+{b}*x')
        print(f'Ajuste logarítmico: ({c})({d}^x)')
        print(f'Factor de distribución direccional: {FA}')
        print(f'Factor carril: {FB}')
        print(f'TPD: {tpd}')
        print(f'TPD acumulado: {tacum}')
        print(f'Factor camión camión: {fcc}')
        print(f'Factor camión: {fc}')
        print(f'Ejes equivalentes: {w18}')
        print(niveltransito(w18))
        print('-------------------------------------')

    reporte()
##------------------------------------------------------------------------------------##

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
y = [1885, 2745, 1626, 1926, 1811, 1684, 1392, 2278, 2199, 2361, 2600, 2969, 2784, 2564, 2863, 2584, 2545, 3077, 2253]

a = [0, 1, 2, 3, 4, 5]
b = [2322, 2327, 2368, 2472, 2682, 2789]

# print(0.55*0.7*4950*3.43*365*(((1.040**15)-1)/np.log(1.040)))

print(f'El FECE para C2P = {FECE()[0]}')
print(f'El FECE para C2G = {FECE()[1]}')
print(f'El FECE para C3C4 = {FECE()[2]}')
print(f'El FECE para C5 = {FECE()[3]}')
print(f'El FECE para >C5 = {FECE()[4]}')
print(f'El FECE para Bus = {FECE()[5]}')
print('Total de camiones: 1177')

prueba(x, y)

##Periodo de diseño crítico
#n = (np.log(((20000000*np.log(1.02516))/(0.55*0.9*3.073533323594172*3059.804980201774*365))+1))/np.log(1.02516)

