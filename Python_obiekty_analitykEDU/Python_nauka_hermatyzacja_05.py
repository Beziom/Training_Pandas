#klasa publiczna
#http://analityk.edu.pl/programowanie-obiektowe-w-python-hermetyzacja-enkapsulacja/
class samochód(object):
    """Klasa samochód"""

    def __init__(self):
        self.silnik=False
        self.bieg = 0
        self.prędkość = 0

    def uruchom (self):
        self.silnik = True
    
    def wyłącz(self):
        self.silnik = False

    def bieg_następny(self):
        if self.bieg <= 6:
            self.bieg += 1
        print("Aktualny bieg to", self.bieg)

    def bieg_poprzedni(self):
        if self.bieg >= 0:
            self.bieg -= 1
        print("Aktualny bieg to", self.bieg)

    def przyszpiesz(self):
        if self.silnik == True and self.bieg >0:
            self.prędkość += 10
            print("Przyspieszasz, twoja prędkość to", self.prędkość)
        else:
            print("Włącz silnik")

    def hamuj(self):
        if self.prędkość >= 10:
            self.prędkość -= 10
        else:
            self.prędkość = 0
        print("Wychamowałeś do", self.prędkość)

#Główny program - klasa publiczna
car1 = samochód()
print("\nsamochód".upper()) 
car1.bieg_następny()
car1.przyszpiesz()
car1.uruchom()
car1.przyszpiesz()
car1.przyszpiesz()
car1.bieg_następny()

#Takie zachowanie pozwoliłoby ingerować na starcie w zepsucie klasy jeżeli ustalilibyśmy bieg na -1 albo 7

#Samochód prywatny
class SamochódPrywatny(object):
    """Klasa samochód"""

    def __init__(self):
        self.__silnik=False
        self.__bieg = 0
        self.__prędkość = 0

    def uruchom (self):
        self.__silnik = True
    
    def wyłącz(self):
        self.__silnik = False

    def bieg_następny(self):
        if self.__bieg <= 6:
            self.__bieg += 1
        print("Aktualny bieg to", self.__bieg)

    def bieg_poprzedni(self):
        if self.__bieg >= 0:
            self.__bieg -= 1
        print("Aktualny bieg to", self.__bieg)

    def przyszpiesz(self):
        if self.__silnik == True and self.__bieg >0:
            self.__prędkość += 10
            print("Przyspieszasz, twoja prędkość to", self.__prędkość)
        else:
            print("Włącz silnik")

    def hamuj(self):
        if self.__prędkość >= 10:
            self.__prędkość -= 10
        else:
            self.__prędkość = 0
        print("Wychamowałeś do", self.__prędkość)

car2 = SamochódPrywatny()    
print("\nSamochód prywatny".upper())  
car2.bieg_następny()
car2.przyszpiesz()
car2.uruchom()
car2.przyszpiesz()
car2.przyszpiesz()
car2.bieg_następny()
# print(car2.__silnik)=
#
# Traceback (most recent call last):
#   File "d:\Repozytorium\Kody_Python\Python_obiekty_analitykEDU\Python_nauka_hermatyzacja_05.py", line 99, in <module>
#     print(car2.__silnik)
# AttributeError: 'SamochódPrywatny' object has no attribute '__silnik'