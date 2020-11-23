import random
import time

budzet = 50000


def generator_z_podanego_zakresu(gora, dol):
    ArrayOfData = []
    mGet = 134456
    aGet = 24091
    cGet = 90821
    xGet = time.time()
    ArrayOfData.append(xGet)
    x = ((aGet * ArrayOfData[len(ArrayOfData)-1]) + cGet) % mGet
    finish = (dol + (x) % (gora - dol))
    return finish


def losowanie_ceny_sprzedazy():
    cena = generator_z_podanego_zakresu(5.0, 10.0)
    return cena


def losowanie_koszt_produkcji():
    cena = generator_z_podanego_zakresu(2.0, 3.0)
    return cena


def losowanie_produkcji():
    produkcja = generator_z_podanego_zakresu(1000, 2000)
    return produkcja


def symulacja_zysku():
    zysk = 0
    for i in range(999):
        zysk_ze_sprzedazy = 0
        koszt_produkcji = losowanie_koszt_produkcji()
        cena_sprzedazy = losowanie_ceny_sprzedazy()
        for j in range(11):
            sztuki = losowanie_produkcji()
            zysk_ze_sprzedazy += (cena_sprzedazy - koszt_produkcji) * sztuki
        zysk += (zysk_ze_sprzedazy - budzet)
    print(f'planowany zysk ze sprzedaży {zysk/1000 }')
    return zysk


if __name__ == "__main__":
    symulacja_zysku()
