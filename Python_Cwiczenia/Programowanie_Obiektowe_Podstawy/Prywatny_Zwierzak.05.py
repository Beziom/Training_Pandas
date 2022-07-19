#Zwierzak posiadający prywatne oraz ubliczne atybuty oraz metody
#Dwa znaki podreślenie stanowią informację że jest to atrybut/metoda prywatna
#Metod prywatnych nie powinno się wyświetlać


#Tworzenie klasy
class Critter(object):
    """Wirtualny Pupil"""
    def __init__(self, name, mood):
        print("Urodził się nowy zwierzak!")
        self.name = name # atrybut publiczny
        self.__mood = mood # atrybut prywatny

    def talk(self):
        print("Jestem", self.name)
        print("W tej chwili czuje się", self.__mood, "/n")

    def __private_method(self):
        print("To jest metoda prywatna")

    def public_method(self):
        print("To jest metoda publiczna")
        self.__private_method()

#Główny program
crit = Critter(name = "Reksio", mood = "szczęśliwy")

crit.talk()
crit.public_method()
 
print()
crit._Critter__mood #Wyświetlenie atrybutu prywatnego
crit._Critter__private_method() #Wyświetlanie atrybutu prywatnego