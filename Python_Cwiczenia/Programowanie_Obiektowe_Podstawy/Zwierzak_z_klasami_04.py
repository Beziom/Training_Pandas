#Wykorzystanie klasy i metod statystycznych
#@static methond


from random import randint, random


class Critter(object):
    """Wirtualny pupil"""
    total = 0 #atrybut o nazwie total
    
    @staticmethod # Dekorator
    def status(): # Nie zawiera zmiennej self (wywoływana przez klasę a nie obiekt)
        print("\nOgólna liczba zwierzaków wynosi", Critter.total)
    
    def __init__ (self, name):
        print("Urodził się nowy zwierzak!")
        Critter.total += 1
        self.name = name

#Część główna
Critter.status()
crit1 = Critter("Zwierzak1")
crit2 = Critter("Zwierzak2")
crit3 = Critter("Zwierzak3")

Critter.status() #Ogólna liczba zwierzaków wynosi 3

print("Uzyskanie dostępu do atrybutu klasy poprzez obiekt:", end = " ")
print(crit1.total) # Uzyskanie dostępu do atrybutu klasy poprzez obiekt: 3

input("Zakończ Enterem")