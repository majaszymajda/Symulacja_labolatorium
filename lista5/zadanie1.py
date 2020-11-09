import math
import random

liczba_pkt_podzialowych = 100


def funkcja1(x):
    return math.exp(-(x**2)/2)


def funkcja2(x):
    return 1-x**2


def funkcja3(x):
    return x**2 + 2*x


def metoda_monte_carlo(xp, xk, dx):
    s = 0
    for i in range(liczba_pkt_podzialowych):
        xlos = random.uniform(xp, xk)
        # print(xlos)
        if xk == xk1:
            s = s + funkcja1(xlos)
            s = s/liczba_pkt_podzialowych*dx1
        elif xk == xk2:
            s = s + funkcja2(xlos)
            s = s/liczba_pkt_podzialowych*dx2

    return s


if __name__ == "__main__":
    xp1 = 0
    xk1 = 1
    xp2 = 0
    xk2 = 2

    dx1 = xk1 - xp1
    dx2 = xk2 - xp2

    print(metoda_monte_carlo(xp1, xk1, dx1))
    print(metoda_monte_carlo(xp2, xk2, dx2))


