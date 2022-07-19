#Podstawy pisania obiektów


class Czlowiek(object):
    """Wirtualny szkic człowieka"""

    def __init__(self, imie, plec, wiek):

        self.imie = imie
        self.plec = plec
        self.wiek = wiek

    def obiekt_informacje(self):
        atributes = [self.imie,self.plec,self.wiek]
        atributes_name = ["Imię", "Płeć", "Wiek"]

        for i,j in zip(atributes, atributes_name):
                print(i,j)

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

human1 = Czlowiek("Andrzej","kobieta",25)
human1.obiekt_informacje()
human1.przywitaj_sie()
human1.ruszaj()
human1.mysl()
