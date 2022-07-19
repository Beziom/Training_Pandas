#Tworzenie klasy - podstawowy zwierzak

#Tworzenie klasy
class Critter(object):                                      #Nazwy klas piszemy z dużej litery, klasa oparta na podstawowym typie object
    """Wirtualny Pupil"""                                   #Łańcuh dokumentacyjny
    def talk(self):                                         #Definiowanie metody (funkcja związana z obiektem), Metoda instacji ma każdy obiekt klasy musi mieć specjlany pierwszy parametr
        print("Cześć! Jestem zwierzątkiem z klas Critter") 

#Inicjacja
pupil = Critter()   #Konkretyzacja obiektu
pupil.talk()        #wywołanie funkcji

input("Aby zakończyć wciśnij Enter")