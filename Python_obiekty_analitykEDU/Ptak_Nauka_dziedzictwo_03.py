#Podstawy dziedziczenia
# class Orzeł(Ptak):
# super().__init__("orzeł", szybkosc)
class Ptak(object):
    """Wirtualny Ptak"""

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lec(self):
        print("Tutaj", self.gatunek, "wznosze się i lecę z szybkością", self.szybkosc)
        print()
    def wydajodglos(self):
        pass

class Orzeł(Ptak):

    def __init__(self, szybkosc):
        super().__init__("orzeł", szybkosc) # funkcja super wprowadza modyfikacją do kodu pozwalając na dziedziczonemu obiektowi wprowadzić własne zmiany

    def poluj(self):
        print("Jestem", self.gatunek, "i napierdzielam do polowania")
        print()

class Pingwin(Ptak):

    def __init__(self,szybkosc):
        super().__init__("pingwin", szybkosc)

    def slizgaj(self):
        print("Tutaj", self.gatunek, "i robiś ślizgu ślizgu")
        print()

    def lec(self):
        print("Tutaj", self.gatunek, "nie polece bo nie umiem")
        print()

orzeł = Orzeł(80)
pingwin = Pingwin(30)

orzeł.lec()
orzeł.poluj()
pingwin.slizgaj()
pingwin.lec()

