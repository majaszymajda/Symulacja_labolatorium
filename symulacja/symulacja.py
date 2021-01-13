from random import randint, random

liczba_pociagow = randint(150, 300)

tablica_wynikow = []
# liczba_pociagow = 100
dalekobiezne_pociagi = 2
lokalne_pociagi = 4


def losowanie():
    los = random()
    if los <= 0.7:
        return 1
    else:
        return 0


class Pociag:
    typy = ['dalekobiezny', 'lokalny']
    typ: str
    zajetosc: int
    wjazd: int

    def __init__(self):
        self.typ = self.typy[losowanie()]
        # 0 - dalekobiezny
        # 1 - lokalny
        if self.typ == 0:
            self.zajetosc = randint(10, 15)
        else:
            self.zajetosc = randint(2, 7)
        self.wjazd = 0

    def __str__(self):
        return f'Pociag typ: {self.typ} - zajętość - {self.zajetosc} - godzina {self.wjazd}'


class Peron:
    nr: int
    typ: str
    zajetosc: int

    _counter = 1

    def __init__(self, typ):
        self.nr = self._counter
        Peron._counter = self._counter + 1
        self.typ = typ
        self.zajetosc = 0

    def __str__(self):
        return f'Peron nr. {self.nr} - {self.typ} - zajętość - {self.zajetosc}'

    def czy_wolne(self):
        return self.zajetosc == 0

    def dodaj_pociag(self, pociag):
        self.zajetosc = pociag.zajetosc

    def zmniejsz_zajetosc(self):
        if (self.zajetosc > 0):
            self.zajetosc = self.zajetosc - 1


perony = [Peron('oczekujący')]

for i in range(dalekobiezne_pociagi):
    perony.append(Peron('dalekobiezny'))
for i in range(lokalne_pociagi):
    perony.append(Peron('lokalny'))


# sprawdzanie wolnego peronu dla pociagu danego typu
def znajdz_wolne(pociag: Pociag):
    typ = pociag.typ
    for peron in perony:
        if (peron.typ == typ) and peron.czy_wolne():
            return peron
    return None


# redukcja zajetosci peronu
def zmniejsz_zajetosci():
    for peron in perony:
        peron.zmniejsz_zajetosc()


def wypisz_analize(licznik, lista, ilosc_do_obsluzenia, obsluzone_pociagi):
    if licznik != 0 and licznik % 240 == 0:
        czy_warunek_spelniony = False
        godzina = licznik // 60
        planowana_obsluga = 0
        if godzina == 4:
            planowana_obsluga = 0.15 * liczba_pociagow
            if len(obsluzone_pociagi) >= int(0.15 * liczba_pociagow):
                czy_warunek_spelniony = True
        elif godzina == 8:
            planowana_obsluga = 0.30 * liczba_pociagow
            if len(obsluzone_pociagi) >= int(0.30 * liczba_pociagow):
                czy_warunek_spelniony = True
        elif godzina == 12:
            planowana_obsluga = 0.5 * liczba_pociagow
            if len(obsluzone_pociagi) >= int(0.5 * liczba_pociagow):
                czy_warunek_spelniony = True
        elif godzina == 16:
            planowana_obsluga = 0.65 * liczba_pociagow
            if len(obsluzone_pociagi) >= int(0.65 * liczba_pociagow):
                czy_warunek_spelniony = True
        elif godzina == 20:
            planowana_obsluga = 0.85 * liczba_pociagow
            if len(obsluzone_pociagi) >= int(0.85 * liczba_pociagow):
                czy_warunek_spelniony = True
        elif godzina == 24:
            planowana_obsluga = liczba_pociagow
            if len(obsluzone_pociagi) >= int(liczba_pociagow):
                czy_warunek_spelniony = True

        nieobsluzone = (int(planowana_obsluga) - len(obsluzone_pociagi))/int(planowana_obsluga) * 100
        if nieobsluzone < 0.0:
            nieobsluzone = 0
        wyniki = {'godzina': godzina, 'nieobsluzone': nieobsluzone}
        tablica_wynikow.append(wyniki)
        print('Godziny od', godzina-4, 'do', godzina, '\n',
              f'Ilość pociągów przyjeżdzających: {int(planowana_obsluga)}', '\n',
              'Ilosc pociagow do obsłużenia: ', len(lista), '\n',
              f'Ilosc pociagow obsluzonych:  {len(obsluzone_pociagi)}', '\n',
              f'Nieobsłużone pociagi: {round(nieobsluzone,2)}%')

        if czy_warunek_spelniony is True:
            print('Udało sie obsłuzyć zakładana liczbe pociagów!')

        print('...................................')


lista_pociagow = []
godzina = 0
for i in range(liczba_pociagow):
    if i <= int(0.15 * liczba_pociagow):
        pociag = Pociag()
        godzina += 2
        pociag.wjazd = godzina
        lista_pociagow.append(pociag)
    elif i <= int(0.30 * liczba_pociagow) and i > int(0.15 * liczba_pociagow):
        if godzina < 240:
            godzina = 240
        pociag = Pociag()
        godzina += 2
        pociag.wjazd = godzina
        lista_pociagow.append(pociag)
    elif i <= int(0.50 * liczba_pociagow) and i > int(0.30 * liczba_pociagow):
        if godzina < 480:
            godzina = 480
        pociag = Pociag()
        godzina += 2
        pociag.wjazd = godzina
        lista_pociagow.append(pociag)
    elif i <= int(0.65 * liczba_pociagow) and i > int(0.50 * liczba_pociagow):
        if godzina < 720:
            godzina = 720
        pociag = Pociag()
        godzina += 2
        pociag.wjazd = godzina
        lista_pociagow.append(pociag)
    elif i <= int(0.85 * liczba_pociagow) and i > int(0.65 * liczba_pociagow):
        if godzina < 960:
            godzina = 960
        pociag = Pociag()
        godzina += 2
        pociag.wjazd = godzina
        lista_pociagow.append(pociag)
    else:
        if godzina < 1200:
            godzina = 1200
        pociag = Pociag()
        godzina += 2
        pociag.wjazd = godzina
        lista_pociagow.append(pociag)


def oblugiwanie_dworca(lista):
    ilosc_do_obsluzenia = len(lista)
    print('Ilosc pociagow do obsłużenia: ', ilosc_do_obsluzenia)
    print('...................................')
    licznik = -1
    obsluzone_pociagi = []
    flag = False
    for pociag in lista:
        while pociag.wjazd != licznik:
            licznik += 1
            zmniejsz_zajetosci()
            wypisz_analize(licznik, lista, ilosc_do_obsluzenia, obsluzone_pociagi)

        if pociag.wjazd == licznik:
            peron = znajdz_wolne(pociag)
            if peron:
                obsluzone_pociagi.append(pociag)
                peron.dodaj_pociag(pociag)
            zmniejsz_zajetosci()
            if len(obsluzone_pociagi) == ilosc_do_obsluzenia:
                print('Obsłużono wszystkie pociagi w czasie', licznik / 60)
                flag = True
    if flag is False:
        while licznik != 1440:
            licznik += 1
            zmniejsz_zajetosci()
        if licznik == 1440:
            wypisz_analize(licznik, lista, ilosc_do_obsluzenia, obsluzone_pociagi)
            procent_nieobsluzonych = format((len(lista) - len(obsluzone_pociagi))/ len(lista) * 100, '.2f')
            print('Nie udało się obsłużyć wsyztskich pociagów w podanym czasie.', '\n',
                  f'Pozostało {len(lista) - len(obsluzone_pociagi)} pociagów do obsłużenia', '\n',
                  f'Nie obsłużono {procent_nieobsluzonych}% pociągów.')


if __name__ == "__main__":
    # print('Rozpopczynam obsługę pociagów')
    # global liczba_pociagow
    oblugiwanie_dworca(lista_pociagow)
    # return tablica_wynikow
