import random


budowa_dworca = {
        'Perony': {
            'dalekobiezne': 2,
            'lokalne': 4,
            'postojowe': 2},
        'dlugosc_peronu': 300
        }

pociag = {
    'dlugosc_lokomotywy': 20,
    'dlugosc_wagonu': 20
}

dlugosc_lokalnego_pociagu = [2, 5]
czas_postoju_lok = [5, 10]

dlugosc_dalekobiezny_pociagu = [7, 12]
czas_postoju_dal = [15, 30]



pociagi_lokalne = []
pociag_dalekobiezne = []
dobowa_ilosc_lokalnych = 0
dobowa_ilosc_dalekobieznych = 0


def losowanie_pociagow(rodzaj, pora):
    # dane_o_pociagu = []
    if rodzaj == 'lokalne':
        poczatek = dlugosc_lokalnego_pociagu[0]
        koniec = dlugosc_lokalnego_pociagu[1]
        poczatek_d = czas_postoju_lok[0]
        koniec_d = czas_postoju_lok[1]
    else:
        poczatek = dlugosc_dalekobiezny_pociagu[0]
        koniec = dlugosc_dalekobiezny_pociagu[1]
        poczatek_d = czas_postoju_lok[0]
        koniec_d = czas_postoju_lok[1]

    ilosc_wagonow = random.randint(poczatek, koniec)

    czas_postoju = random.randint(poczatek_d, koniec_d)


    print({'ilosc_wagonow': ilosc_wagonow, 'czas_postoju': czas_postoju, 'rodzaj': rodzaj, 'pora_przyjazdu': pora})
    return {'ilosc_wagonow': ilosc_wagonow, 'czas_postoju': czas_postoju, 'rodzaj': rodzaj, 'pora_przyjazdu': pora}


def generowanie_pociagu():
    dobowa_ilosc_pociagow = random.randint(80, 100)
    dobowa_ilosc_lokalnych = int(0.7 * dobowa_ilosc_pociagow)
    dobowa_ilosc_dalekobieznych = dobowa_ilosc_pociagow - dobowa_ilosc_lokalnych
    # suma = dobowa_ilosc_dalekobieznych + dobowa_ilosc_lokalnych
    # lok = lokalne['ilosc_wagonow']
    for pociag in range(dobowa_ilosc_lokalnych):
        if pociag <= int(0.1 * dobowa_ilosc_lokalnych):
            pora = 1
        elif pociag <= int(0.25 * dobowa_ilosc_lokalnych) and pociag > int(0.1 * dobowa_ilosc_lokalnych):
            pora = 2
        elif pociag <= int(0.55 * dobowa_ilosc_lokalnych) and pociag > int(0.25 * dobowa_ilosc_lokalnych):
            pora = 3
        elif pociag <= int(0.7 * dobowa_ilosc_lokalnych) and pociag > int(0.55 * dobowa_ilosc_lokalnych):
            pora = 4
        else:
            pora = 5
        pociagi_lokalne.append(losowanie_pociagow('lokalne', pora))

    for pociag in range(dobowa_ilosc_dalekobieznych):
        if pociag <= int(0.1 * dobowa_ilosc_lokalnych):
            pora = 1
        elif pociag <= int(0.25 * dobowa_ilosc_lokalnych) and pociag > int(0.1 * dobowa_ilosc_lokalnych):
            pora = 2
        elif pociag <= int(0.55 * dobowa_ilosc_lokalnych) and pociag > int(0.25 * dobowa_ilosc_lokalnych):
            pora = 3
        elif pociag <= int(0.7 * dobowa_ilosc_lokalnych) and pociag > int(0.55 * dobowa_ilosc_lokalnych):
            pora = 4
        else:
            pora = 5
        pociag_dalekobiezne.append(losowanie_pociagow('dalekobiezne', pora))

    return pociagi_lokalne, pociag_dalekobiezne


if __name__ == "__main__":
    generowanie_pociagu()
