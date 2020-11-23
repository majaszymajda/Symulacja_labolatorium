import random


def generator(numbers):
    a = 226954477
    c = 71917
    m = pow(2, 32)
    seed = 4359
    x = (seed * a + c) % m
    u = []
    u.append(abs((2*x/m)-1))
    for i in range((numbers-1)):
        x = (x * a + c) % m
        u.append(abs((2 * x / m) - 1))
    # print(u)
    return u


def generator_normalny():
    a = 58363
    c = 71917
    m = 102259
    seed = 4359
    temp = []
    x = (seed*a+c) % m
    temp.append(x/m)
    for i in range(239):
        x = (x * a + c) % m
        temp.append(x/m)
    NN = []

    for i in range(0, 240, 12):
        NN.append(abs(((sum(temp[i:i+11]))-6) * 0.5 + 0.5))
    # print (( (sum(temp[i:j]) ) - 6 ) * 0.5 + 0.5)
    # print(NN)
    return NN


def losowanie_wagi_elementow(ilosc_elementow):
    waga_elementow = []
    zbior = generator_normalny()
    for i in range(ilosc_elementow):
        waga_elementow.append(zbior[i]*2)

    return waga_elementow


def f_zero_jeden(x):
    if (x < 0,5):
        return 1
    else:
        return 0


def zbior_0_1(zbior_wykorzystania):
    macierz = []
    print(zbior_wykorzystania)
    for i in range(len(zbior_wykorzystania)):
        macierz.append(f_zero_jeden(zbior_wykorzystania[i]))
        print(macierz[i])
    return macierz


def zbior_0_1_(zbior_wykorzystania):
    macierz = []
    for i in range(len(zbior_wykorzystania)):
        macierz.append(random.randint(0, 1))

    return macierz


def problem_plecakowy(pojemnosc, ilosc_elementow, waga_elementow):
    proby_udane = 0
    proby_nieudane = 0
    wszystkie_proby = 0
    for i in range(2000):
        suma = 0
        zbior = generator(ilosc_elementow)
        macierz_wykorzystania = zbior_0_1_(zbior)
        # print(macierz_wykorzystania)
        for j in range(ilosc_elementow-1):
            x = 0.0
            # print(macierz_wykorzystania[i][j])
            x = macierz_wykorzystania[j] * waga_elementow[j]
            suma += x
        if (suma <= pojemnosc):
            proby_udane += 1
        else:
            proby_nieudane += 1
        wszystkie_proby += 1
    # print(proby_udane/wszystkie_proby)
    wynik = proby_udane/wszystkie_proby
    print(f'{wynik* 100}%  oraz {proby_udane}')
    return wynik


if __name__ == "__main__":
    pojemnosc = 10
    ilosc_elementow = 20
    waga_elementow = losowanie_wagi_elementow(ilosc_elementow)
    # print(waga_elementow)
    # macierz_wykorzystania = losowanie_macierzy_wykorzystania(ilosc_elementow)
    problem_plecakowy(pojemnosc, ilosc_elementow, waga_elementow)
