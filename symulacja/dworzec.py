from random import randint
import time
import uuid


# budowa_dworca = {
#         'Perony': {
#             'dalekobiezne': 2,
#             'lokalne': 4,
#             'postojowe': 2},
#         'dlugosc_peronu': 300
#         }

# pociag = {
#     'dlugosc_lokomotywy': 20,
#     'dlugosc_wagonu': 20
# }

# dlugosc_lokalnego_pociagu = [2, 5]
# czas_postoju_lok = [5, 10]

# dlugosc_dalekobiezny_pociagu = [7, 12]
# czas_postoju_dal = [15, 30]

# pociagi_lokalne = []
# pociag_dalekobiezne = []
liczba_pociagow = randint(200, 400)
# dobowa_ilosc_lokalnych = 0
# dobowa_ilosc_dalekobieznych = 0


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


# tworzenie klasy reprezentującej całą listę
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
    godzina_wjazdu: int

    def __init__(self):
        self._id = uuid.uuid1()
        self.typ = self.typy[randint(0, 1)]
        # 0 - dalekobiezny
        # 1 - lokalny
        if self.typ == 0:
            self.zajetosc = randint(20, 45)
        else:
            self.zajetosc = randint(10, 15)
        # self.godzina_wjazdu = randint(0, 230)

    def __str__(self):
        return f'Pociag typ: {self.typ} - zajętość - {self.zajetosc} - godzina {self.godzina_wjazdu}'


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
    Peron('dalekobiezny')
]


# sprawdzanie wolnego peronu dla pociagu danego typu
def znajdz_wolne(pociag: Pociag):
    typ = pociag.typ
    for peron in perony:
        if (peron.typ == typ) and peron.czy_wolne():
            return peron
    return None


# redukcja zajetosci klienta
def zmniejsz_zajetosci():
    for peron in perony:
        peron.zmniejsz_zajetosc()


lista_1 = LinkedList()
lista_2 = LinkedList()
lista_3 = LinkedList()
lista_4 = LinkedList()
lista_5 = LinkedList()
lista_6 = LinkedList()
# zrobic co 0.5 h generowanie list pociagow + zmiana kolejki (mamy harmonogram) + losowe sytuacje?

for i in range(liczba_pociagow):
    if i <= int(0.1 * liczba_pociagow):
        lista_1.insert(Pociag())
    elif i <= int(0.25 * liczba_pociagow) and i > int(0.1 * liczba_pociagow):
        lista_2.insert(Pociag())
    elif i <= int(0.50 * liczba_pociagow) and i > int(0.25 * liczba_pociagow):
        lista_3.insert(Pociag())
    elif i <= int(0.65 * liczba_pociagow) and i > int(0.50 * liczba_pociagow):
        lista_4.insert(Pociag())
    elif i <= int(0.85 * liczba_pociagow) and i > int(0.65 * liczba_pociagow):
        lista_5.insert(Pociag())
    else:
        lista_6.insert(Pociag())


def oblugiwanie_dworca(lista):
    ilosc_do_obsluzenia = lista.size()
    licznik = 0
    while True:
        print('ilosc pociagow oczekujacych: ', lista.size())
        if lista.size() == 0:
            break
        licznik += 1
        obsluzone_pociagi = []
        for pociag in lista:
            # if licznik ==
            peron = znajdz_wolne(pociag)
            if peron:
                obsluzone_pociagi.append(pociag)
                peron.dodaj_pociag(pociag)
        zmniejsz_zajetosci()
        for pociag_1 in obsluzone_pociagi:
            lista.remove(pociag_1)
        for peron in perony:
            print(peron)
        time.sleep(2)
        # print(f'ilosc pociagow obsluzonych:  {ilosc_do_obsluzenia-lista.size()}')
        if ilosc_do_obsluzenia == licznik:
            False
    print('Ilosc iteracji', licznik)


if __name__ == "__main__":
    print('lista 1')
    oblugiwanie_dworca(lista_1)
    for i in range(4):
        print('')
    print('lista 2')
    oblugiwanie_dworca(lista_2)
    for i in range(4):
        print('')
    print('lista 3')
    oblugiwanie_dworca(lista_3)
    for i in range(4):
        print('')
    print('lista 4')
    oblugiwanie_dworca(lista_4)
    for i in range(4):
        print('')
    print('lista 5')
    oblugiwanie_dworca(lista_5)
    for i in range(4):
        print('')
    oblugiwanie_dworca(lista_6)
