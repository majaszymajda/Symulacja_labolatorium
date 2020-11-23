import math
import time


liczba_pkt_podzialowych = 1999


#def generator(numbers):
#    a = 226954477
#    c = 71917
#    m = pow(2, 32)
#    seed = 4359
#    x = (seed * a + c) % m
#    u = []
#    u.append(abs((2*x/m)-1))
#    for i in range(numbers-1):
#        x = (x * a + c) % m
#        u.append(abs((2 * x / m) - 1))
#    return u


def generator(param, xp, xk):
    ArrayOfData = []
    mGet = 134456
    aGet = 24091
    cGet = 90821
    xGet = time.time()
    dol = xp
    gora = xk
    ArrayOfData.append(xGet)

    for index in range(param):
        xi = ((aGet * ArrayOfData[len(ArrayOfData)-1]) + cGet) % mGet
        finish = (dol + (xi) % (gora - dol))
        if index == 0:
            ArrayOfData.clear()
        ArrayOfData.append(finish)
    return ArrayOfData


def funkcje(x, ktora_funkcja):
    if (ktora_funkcja == 1):
        f1 = math.exp(-(x**2)/2)
        return f1
    else:
        f2 = 1-x**2
        return f2


def funkcja3(x):
    return x**2 + 2*x


def metoda_monte_carlo(xp, xk, dx):
    LP1 = 0
    LPP1 = 0
    zbior_punktow = []
    for j in range(liczba_pkt_podzialowych):
        zbior_punktow.append(generator(liczba_pkt_podzialowych, xp, xk)[j])
    for i in range(1000):

    # zbiór_punktow = generator(liczba_pkt_podzialowych)
        if(zbior_punktow[+1] <= funkcje(zbior_punktow[i], xk)):
            LPP1 += 1
        LP1 += 1

    return LPP1/LP1


if __name__ == "__main__":
    xp1 = 0
    xk1 = 1
    xp2 = 0
    xk2 = 2

    dx1 = xk1 - xp1
    dx2 = xk2 - xp2

    print(metoda_monte_carlo(xp1, xk1, dx1))
    print(metoda_monte_carlo(xp2, xk2, dx2))


