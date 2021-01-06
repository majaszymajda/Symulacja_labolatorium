from random import randint, randrange
# import time
import uuid

# liczba_pociagow = randint(200, 400)
liczba_pociagow = 200


# węzeł kolejki
class Node():

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


# klasa tworząca kolejke
class LinkedList():

    def __init__(self):
        self.start_node = None

    def insert(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.next_node is not None:
            n = n.next_node
        n.next_node = new_node

    def remove(self, key):
        temp = self.start_node
        if (temp is not None):
            if (temp.data._id == key._id):
                self.start_node = temp.next_node
                temp = None
                return
        while(temp is not None):
            if temp.data._id == key._id:
                break
            prev = temp
            temp = temp.next_node

        if(temp is None):
            return

        prev.next_node = temp.next_node
        temp = None

    def size(self):
        counter = 0
        if self.start_node is None:
            return counter
        else:
            n = self.start_node
            while n is not None:
                counter += 1
                n = n.next_node
        return counter

    def __iter__(self):
        self.current_node = self.start_node
        return self

    def __next__(self):
        if self.current_node is None:
            raise StopIteration
        else:
            result = self.current_node.data
            self.current_node = self.current_node.next_node
            return result


class Pociag:

    typy = ['dalekobiezny', 'lokalny']
    typ: str
    zajetosc: int
    wjazd: int

    def __init__(self):
        self._id = uuid.uuid1()
        self.typ = self.typy[randint(0, 1)]
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


perony = [
    Peron('lokalny'),
    Peron('lokalny'),
    Peron('lokalny'),
    Peron('lokalny'),
    Peron('dalekobiezny'),
    Peron('dalekobiezny'),
    Peron('oczekujący')

]


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
        print('Godziny od', godzina-4, 'do', godzina, '\n',
              'Ilosc pociagow do obsłużenia: ', lista.size(), '\n',
              f'Ilosc pociagow obsluzonych:  {ilosc_do_obsluzenia - lista.size()}')
        if godzina == 4 and len(obsluzone_pociagi) >= int(0.15 * liczba_pociagow):
            czy_warunek_spelniony = True
        elif godzina == 8 and len(obsluzone_pociagi) >= int(0.30 * liczba_pociagow):
            czy_warunek_spelniony = True
        elif godzina == 12 and len(obsluzone_pociagi) >= int(0.5 * liczba_pociagow):
            czy_warunek_spelniony = True
        elif godzina == 16 and len(obsluzone_pociagi) >= int(0.65 * liczba_pociagow):
            czy_warunek_spelniony = True
        elif godzina == 20 and len(obsluzone_pociagi) >= int(0.85 * liczba_pociagow):
            czy_warunek_spelniony = True
        elif godzina > 20 and len(obsluzone_pociagi) >= int(liczba_pociagow):
            czy_warunek_spelniony = True

        if czy_warunek_spelniony is True:
            print('Udało sie obsłuzyć zakładana liczbe pociagów')
        else:
            print('Nie udalo sie obsłuzyc zakladanej liczby pociagow')

        print('...................................')


lista_pociagow = LinkedList()
godzina = 0
for i in range(liczba_pociagow):
    if i <= int(0.15 * liczba_pociagow):
        pociag = Pociag()
        godzina += 2
        pociag.wjazd = godzina
        lista_pociagow.insert(pociag)
    elif i <= int(0.30 * liczba_pociagow) and i > int(0.15 * liczba_pociagow):
        if godzina < 240:
            godzina = 240
        pociag = Pociag()
        godzina += 2
        pociag.wjazd = godzina
        lista_pociagow.insert(pociag)
    elif i <= int(0.50 * liczba_pociagow) and i > int(0.30 * liczba_pociagow):
        if godzina < 480:
            godzina = 480
        pociag = Pociag()
        godzina += 2
        pociag.wjazd = godzina
        lista_pociagow.insert(pociag)
    elif i <= int(0.65 * liczba_pociagow) and i > int(0.50 * liczba_pociagow):
        if godzina < 720:
            godzina = 720
        pociag = Pociag()
        godzina += 2
        pociag.wjazd = godzina
        lista_pociagow.insert(pociag)
    elif i <= int(0.85 * liczba_pociagow) and i > int(0.65 * liczba_pociagow):
        if godzina < 960:
            godzina = 960
        pociag = Pociag()
        godzina += 2
        pociag.wjazd = godzina
        lista_pociagow.insert(pociag)
    else:
        if godzina < 1200:
            godzina = 1200
        pociag = Pociag()
        godzina += 2
        pociag.wjazd = godzina
        lista_pociagow.insert(pociag)


def oblugiwanie_dworca(lista):
    ilosc_do_obsluzenia = lista.size()
    print('Ilosc pociagow do obsłużenia: ', lista.size())
    print('...................................')
    licznik = 0
    obsluzone_pociagi = []
    for pociag in lista:
        while pociag.wjazd != licznik:
            if len(obsluzone_pociagi) == ilosc_do_obsluzenia:
                print('Obsłużono wszystkie pociagi w czasie', licznik / 60)
            if licznik == 1440:
                procent_nieobsluzonych = format(lista.size() / ilosc_do_obsluzenia * 100, '.2f')
                print('Nie udało się obsłużyć wsyztskich pociagów w podanym czasie.', '\n',
                      f'Pozostało {lista.size()} pociagów do obsłużenia', '\n',
                      f'Nie obsłużono {procent_nieobsluzonych}% pociągów.')
                break
            licznik += 1
            # print(licznik)
            zmniejsz_zajetosci()
            wypisz_analize(licznik, lista, ilosc_do_obsluzenia, obsluzone_pociagi)

        if pociag.wjazd == licznik:
            peron = znajdz_wolne(pociag)
            if peron:
                obsluzone_pociagi.append(pociag)
                peron.dodaj_pociag(pociag)
                lista.remove(pociag)
            zmniejsz_zajetosci()


if __name__ == "__main__":
    print('Rozpopczynam obsługę pociagów')
    oblugiwanie_dworca(lista_pociagow)

