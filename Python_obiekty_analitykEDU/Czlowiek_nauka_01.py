#Podstawy pisania obiektów
class Czlowiek(object):
    """Wirtualny szkic człowieka"""

    imie = ""
    wiek = None
    plec = ""

    def przywitaj_sie(self):
        print("Cześć, mam na imię", self.imie)

    def ruszaj(self):
        if self.plec == "kobieta":
            print("Ruszyłem się")
        else:
            print("Ruszyłem w drogę")

    def mysl(self):
        if self.wiek < 2:
            print("Dopiero się uczę")
        else:
            print("Nie ma żadnego problemu")

human1 = Czlowiek()
human1.imie = "Andrzej"
human1.wiek = 20
human1.plec = "mężczyzna"
human1.przywitaj_sie()
human1.ruszaj()
human1.mysl()
