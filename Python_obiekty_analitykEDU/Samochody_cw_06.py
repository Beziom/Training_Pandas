class samochód(object):
    """Klasa samochód"""

    def __init__(self):
        self.__silnik=False
        self.__bieg = 0
        self.__prędkość = 0

    def uruchom (self):
        self.__silnik = True
    
    def wyłącz(self):
        self.__silnik = False

    def __bieg_następny(self):
        if self.__bieg <= 6:
            self.__bieg += 1
        print("Aktualny bieg to", self.__bieg)

    def __bieg_poprzedni(self):
        if self.__bieg >= 0:
            self.__bieg -= 1
        print("Aktualny bieg to", self.__bieg)

    def przyszpiesz(self):
        if self.__silnik == True:
            self.__prędkość += 10
            print("Przyspieszasz, twoja prędkość to", self.__prędkość)
        else:
            print("Włącz silnik")
        
        self.__bieg_następny()

    def hamuj(self):
        if self.__prędkość >= 10:
            self.__prędkość -= 10
        else:
            self.__prędkość = 0
        print("Wychamowałeś do", self.__prędkość)

        self.__bieg_poprzedni()

#Main
car1 = samochód()
print("\nsamochód".upper()) 
car1.przyszpiesz()
car1.uruchom()
car1.przyszpiesz()
car1.przyszpiesz()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.przyszpiesz()