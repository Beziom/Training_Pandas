# Musi mieć możliwość przechowywania notatek oraz wizytówek
# Po uruchomieniu, powinno wyświetlać się menu, które pozwala użytkownikowi: (1) – dodać notatkę (2) – dodać wizytówkę (3) wyświetlić notatki (4) – wyświetlić wizytówki (0) zamknąć organizer, a tym samym zakończyć działanie programu
# Program powinien być podzielony na moduły, czyli plik

from abc import ABC, abstractmethod


class Organizer(object):
    """Wirtualny organizer"""

    __wlasciciel = ""
    __baza_danych = []

    def __init__(self, wlasciciel):
        self.wlasciciel = wlasciciel

    def dodaj_notatke(self):
        priorytet = input("Priorytet:")
        tytuł = input("Tytuł:")
        treść = input("Treść:")

        nowaNotatka = notatka(priorytet, tytuł, treść)
        self.__baza_danych.append(nowaNotatka)

    def dodaj_wizytowke(self):
        priorytet = input("Priorytet:")
        imię = input("Imię:")
        nazwisko = input("Nazwisko:")
        telefon = input("Telefon:")

        nowaWizytówka = wizytowka(priorytet, imię, nazwisko, telefon)
        self.__baza_danych.append(nowaWizytówka)

    def wyswietl_notatke(self):

        print("Lista notatek\n")
        for i in self.__baza_danych:
            if i.typ == "Notatka":
                print(i)

    def wyswietl_wizytowke(self):
        print("Lista wizytówek\n")
        for i in self.__baza_danych:
            if i.typ == "Wizytowka":
                print(i)


class przedmiot(ABC):

    def __init__(self, typ, priorytet):
        self.typ = typ
        self.priorytet = priorytet

    @abstractmethod
    def __str__(self):  # obiekt może być obsłużony funkcją print - print(notatka) albo print(wizytówka)
        pass


class notatka(przedmiot):
    """Wirtualna notatka"""

    def __init__(self, priorytet, tytuł, treść):
        super().__init__("Notatka", priorytet)
        self.tytuł = tytuł
        self.treść = treść

    def __str__(self):
        info = self.typ + "Prioytet " + self.priorytet + "\n"
        info += self.tytuł + "\n"
        info += self.treść + "\n"
        return info


class wizytowka(przedmiot):

    def __init__(self, priorytet, imie, nazwisko, telefon):
        super().__init__("Wizytowka", priorytet)
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon

    def __str__(self):
        info = self.typ + "Prioytet " + self.priorytet + "\n"
        info += self.imie + " " + self.nazwisko + "\n"
        info += self.telefon + "\n"
        return info

# notatka ora przedmiot nadpisują metodę specjalną __str__


organizer = Organizer("Maciej Siewierski")

while True:

    print("""Co chcesz zrobić?
    1 - dodać notatką
    2 - dodać wizytówkę
    3 - wyświetlić notatkę
    4 - wyświetlić wizytówkę
    5 - zamknąć program """)
    x = int(input())

    if x == 1:
        organizer.dodaj_notatke()
    elif x == 2:
        organizer.dodaj_wizytowke()
    elif x == 3:
        organizer.wyswietl_notatke()
    elif x == 4:
        organizer.wyswietl_wizytowke()
    elif x == 5:
        print("Dziękujemy!")
        break
