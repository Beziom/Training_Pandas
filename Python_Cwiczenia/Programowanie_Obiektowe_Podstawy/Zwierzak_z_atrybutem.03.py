#Zwierzak z wykorzystanie atrybutów
#self - automatycznie otrzymuje jako swoją wartość referncję do obiektu wywoującego metodę. Dzięki niemu można sięgnąć do wywołującego ją obietku i uzyska dostęp do atrybutu i metod
#notacja z kropką jest używana aby uzyskac dostęp do klasy
#__str__() zwraca łańcuh który zawiera wartość atrybutu name obiektu

#Tworzenie klasy
class Critter(object):
    """Zwierzak klasy Pupil"""
    def __init__(self, name): # nadanie zostajy nowy atrybut name
        print("Urodził się nowy zwierzak")
        self.name = name #Tworzenie atrybutu name dla obiektu i nadanie mu wartości name

    def __str__(self):                          #Specjalne metoda Bez tej metody wystąpiłby kod podczas print(crit1) = <__main__.Critter object at 0x00A0BA90>
        rep = "Obiekt klady Critter\n"
        rep += "name: " + self.name + "\n"
        return rep

    def talk(self):
        print("Cześć! Jestem", self.name, "\n")

#Główna część
print()
crit1 = Critter(name = "Reksio")
crit1.talk()

crit2 = Critter(name = "Dyzio")
crit2.talk()

print("Wyświetlenie obiektu crit1:")
print(crit1)

print("Bezpośrednie wyświetlenie wartości atrybutu crit1.name:")
print(crit1.name) #notacja z kropką jest używana aby uzyskac dostęp do klasy

input("Zakończ Enterkiem")