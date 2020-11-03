import matplotlib.pyplot as plt
from math import sqrt
import scipy.stats.mstats
import statistics
import numpy as np
import scipy
import time

hipoteza = 0.7
zbior = []
elements = 20
# elements = 100


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


zbior = generator(elements)


def srednia(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


def harmoniczna(numbers):
    sum = 0
    for number in numbers:
        sum += 1 / number
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


def test_shapiro_wilka(numbers):
    test = scipy.stats.shapiro(numbers)
    return test
    

if __name__ == "__main__":
    print(generator(elements))
    print(f"Średnia arytmetyczna: {srednia(zbior)}")
    print(f"Średnia harmoniczna: {round(harmoniczna(zbior), 2)}")
    print(f"Odchylenie standardowe: {round(statistics.stdev(zbior), 5)}, druga metoda: {round(np.std(zbior), 5)}")
    print(f"Wariancja: {round(wariancja(zbior, srednia(zbior)), 4)}")
    print(f"Dominanta: {moda_main(zbior)}")
    print(f"skośność: {skosnosc_f(zbior)}")
    print(f"Kurtoza: {kurtoza_f(zbior)}")
    print(f'test t studenta: {test_t_studenta(srednia(zbior), hipoteza, statistics.stdev(zbior))}')
    print(f'test normalnosci rozkladu: {test_shapiro_wilka(zbior)}')
    # print(f'test Z: {test_Z(srednia(zbior), hipoteza, statistics.stdev(zbior))}')
    print(f'histogram: {histogram(zbior)}')
