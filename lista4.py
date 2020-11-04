import matplotlib.pyplot as plt
from math import sqrt
import scipy.stats.mstats
import statistics
import numpy as np
import scipy
import time

hipoteza = 0.7
zbior1 = []
zbior = []
# elements = 20
elements = 100
# a_20 = [0.4734, 0.3211, 0.2565, 0.2085, 0.1686, 0.1334, 0.1013, 0.0711, 0.0422, 0.0140]
a_100 = [0.3158, 0.2089, 0.1892, 0.1752, 0.164, 0.1547, 0.1466, 0.1394, 0.1329, 0.127, 0.1215, 0.1163, 0.1115, 0.1069, 0.1026, 0.0984, 0.0944, 0.0906, 0.0869,
0.0834, 0.0834, 0.0765, 0.0733, 0.0701, 0.067, 0.0639, 0.0609, 0.058, 0.0551, 0.0523, 0.0495, 0.0467, 0.044, 0.0413, 0.0387, 0.0361, 0.0335, 0.0309, 0.0284,
0.0258, 0.0233, 0.0208, 0.0183, 0.0159, 0.0134, 0.011, 0.0083, 0.0061, 0.0037, 0.0012]


def generator(numbers):
    a = 226954477
    c = 1
    m = pow(2, 32)
    x0 = int(time.time()/(100+numbers))
    u = [x0]
    for i in range(numbers-1):
        u.append((a*u[i] + c) % m)
    L = np.array(u)
    L = 1/m * L
    return L


zbior1 = generator(elements)


def rozklad_normalny(numbers, zbior1):
    zbior = []
    for i in range(int(elements/2)):
        x1 = zbior1[i+i]
        x2 = zbior1[i+i+1]
        # print(x1, x2)
        y1 = np.sqrt(-2 * np.log(x1)) * np.cos(2 * np.pi * x2)
        y2 = np.sqrt(-2 * np.log(x1)) * np.sin(2 * np.pi * x2)
        zbior.append(y1)
        zbior.append(y2)
    # print(zbior)
    return zbior


zbior = rozklad_normalny(elements, zbior1)


def srednia(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


def harmoniczna(numbers):
    sum = 0
    for number in numbers:
        sum += 1 / number
        print(sum)
    return (len(numbers) / sum)


def wariancja(numbers, aver):
    sum = 0
    for number in numbers:
        sum += pow((number - aver), 2)
    return sum / len(numbers)


def indexof(a, A):
    for i in range(len(A)):
        if A[i] == a:
            return i
    return -1


def mode(A):
    liczby = []
    wystapienia = []

    for a in A:
        index = indexof(a, liczby)
        if index >= 0:
            wystapienia[index] += 1
        else:
            liczby.append(a)
            wystapienia.append(1)

    _mode = 0
    count = 0
    for i in range(len(wystapienia)):
        if wystapienia[i] > wystapienia[_mode]:
            _mode = i
            count = 1
        elif wystapienia[i] == wystapienia[_mode]:
            count += 1

    if count == 1:
        return [liczby[_mode], wystapienia[_mode]]
    else:
        return None


def moda_main(numbers):
    m = mode(numbers)
    if m is not None:
        return "Moda: %d, wystapien: %d" % (m[0], m[1])
    else:
        return "Nie znaleziono mody"


def skosnosc_f(numbers):
    skosnosc = scipy.stats.skew(numbers)
    return skosnosc


def kurtoza_f(numbers):
    kurtoza = scipy.stats.kurtosis(numbers)
    return kurtoza


def dominant(numbers):
    sortNumbers = sorted(numbers)
    # print(sortNumbers)
    return sortNumbers[int((len(sortNumbers))/2 - 1)], sortNumbers[int((len(sortNumbers))/2)]


def histogram(numbers):

    plt.hist(numbers, label=elements)
    plt.legend(loc='upper right')
    plt.xlabel('wartosc')
    plt.ylabel('ilosc')
    plt.title('histogram dla ciagow')
    return plt.show()


def test_t_studenta(srednia, hipoteza, odchylenie_st):
    t = ((srednia - hipoteza)/odchylenie_st)*sqrt(elements-1)
    return t


def test_Z(srednia, hipoteza, odchylenie_st):
    Z = ((srednia - hipoteza)/odchylenie_st)*sqrt(elements)
    return Z


def test_shapiro_wilka(numbers, a):
    numbers = sorted(numbers)
    n = len(numbers)

    sum1 = 0
    sum2 = 0
    for i in range(len(a)):
        sum1 += a[i] * (numbers[n-i-1] - numbers[i])
    for j in range(n):
        sum2 += (numbers[j] - np.mean(numbers))**2
    return sum1**2/sum2


def sprawdzenie_testu_shapiro_wilka(numbers):
    test = scipy.stats.shapiro(numbers)
    return test


if __name__ == "__main__":
    print(generator(elements))
    print(rozklad_normalny(elements, zbior1))
    print(f"Średnia arytmetyczna: {srednia(zbior)}")
    print(f"Średnia harmoniczna: {round(harmoniczna(zbior), 2)}")
    print(f"Odchylenie standardowe: {round(statistics.stdev(zbior), 5)}, druga metoda: {round(np.std(zbior), 5)}")
    print(f"Wariancja: {round(wariancja(zbior, srednia(zbior)), 4)}")
    print(f"Dominanta: {moda_main(zbior)}")
    print(f"skośność: {skosnosc_f(zbior)}")
    print(f"Kurtoza: {kurtoza_f(zbior)}")
    print(f'test t studenta: {test_t_studenta(srednia(zbior), hipoteza, statistics.stdev(zbior))}')
    print(f'test normalnosci rozkladu: {test_shapiro_wilka(zbior, a_100)}')
    print(f'test normalnosci rozkladu sprawdzenie: {sprawdzenie_testu_shapiro_wilka(zbior)}')

    # print(f'test Z: {test_Z(srednia(zbior), hipoteza, statistics.stdev(zbior))}')
    print(f'histogram: {histogram(zbior)}')
