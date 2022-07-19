from abc import ABC, abstractmethod

#moduł ABC oraz abstrackmethod z pakietu abc pozwala na towrzenie abstrajcyjnych klas i metod
#metody @abstrackmethod to metoda abstrakcyjna która musi zostać nadpisana przez potomswo, @abstrackmethod to dekorator

#klasy
class Ptak(ABC): #dziedziczenie ABC
    """Wirtualny Ptak"""

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lec(self):
        print("Tutaj", self.gatunek, "wznosze się i lecę z szybkością", self.szybkosc)
    
    @abstractmethod #musi zostać napisany przez dziedziczne klasy
    def wydajodglos(self):
        pass

class Orzeł(Ptak):

    def __init__(self, szybkosc):
        super().__init__("orzeł", szybkosc) # funkcja super wprowadza modyfikacją do kodu pozwalając na dziedziczonemu obiektowi wprowadzić własne zmiany

    def poluj(self):
        print("Jestem", self.gatunek, "i napierdzielam do polowania")

    def wydajodglos(self): # brak metody skutkuje błędem
        print("Wrrrrrr")

class Pingwin(Ptak):

    def __init__(self,szybkosc):
        super().__init__("pingwin", szybkosc)

    def slizgaj(self):
        print("Tutaj", self.gatunek, "i robię ślizgu ślizgu")

    def lec(self):
        print("Tutaj", self.gatunek, "nie polece bo nie umiem")
    
    def wydajodglos(self):
        print("Kłikłik")

#Main
orzeł = Orzeł(80)
pingwin = Pingwin(30)

print()
orzeł.lec()
orzeł.poluj()
print()
pingwin.lec()
pingwin.slizgaj()
print()
orzeł.wydajodglos()
pingwin.wydajodglos()