from abc import ABC, abstractmethod

class jednoślad(ABC):
    """Szkic dla jednośladów"""

    def __init__(self, typ, przebieg, kolor):
        self.typ = typ
        self.przebieg = przebieg
        self.kolor = kolor
    
    def jedź(self):
        przebieg += 1

    def podajPrzebieg(self):
        return self.przebieg

    @abstractmethod
    def dane_pojazdu(self):
        pass
    
class motocykl(jednoślad):

    def __init__(self, przebieg, kolor, silnik):
        super().__init__("Motocykl", przebieg, kolor)
        self.silnik = silnik

    def dane_pojazdu(self):
       data = [self.przebieg, self.kolor, self.silnik]
       for i in data:
        print(i)

class skuter(jednoślad):

    def __init__(self, przebieg, kolor, wersja_silnika):
        super().__init__("Motocykl", przebieg, kolor)
        self.wersja_silnika = wersja_silnika

    def dane_pojazdu(self):
        data = [self.przebieg, self.kolor, self.wersja_silnika]
        for i in data:
         print(i)
    


motocykl1 = motocykl("250tyś km", "czerwony", "1.8skuti")
motocykl1.dane_pojazdu()

skuter1 = skuter(65000,"Jasno Zielony", "Włoski")
skuter1.dane_pojazdu()