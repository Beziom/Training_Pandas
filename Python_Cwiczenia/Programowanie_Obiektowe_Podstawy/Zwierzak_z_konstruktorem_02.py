#Zwierzak z konstruktorem
#Demonstracja konstuktorów
#__init__

#Tworzenie klady
class Critter(object):
    """Wirtualny pupil"""
    def __init__(self): # Metoda inicjalizacji (konstruktor) - wywoływany automatycznie przez kązdy nowo utworzony obiekt klasy Critter
        print("Urodził się nowy zwierzak")

    def talk(self):
        print("\nCześć jestem nowym zwierzątkiem klasy Critter")

pupil1 = Critter() #Dzięki funkcji init przy powstaniu "Rodzi się nowy zwierzak"
pupil2 = Critter()

pupil1.talk() #  wywołanie funkcji
pupil2.talk()

input("Aby zakończyć program wciśnij Enter")