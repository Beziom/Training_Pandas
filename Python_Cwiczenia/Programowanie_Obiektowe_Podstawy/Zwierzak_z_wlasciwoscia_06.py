# Zwierzak z właściwością

# Instrukcja przypisania crit.name = "Pucek" wykorzystuje dostęp do właściwości name
# obiektu i pośrednio wywołuje metodę, która się stara ustawić wartość atrybutu __name.
# W tym przypadku do parametru new_name tej metody zostaje przekazana referencja do
# łańcucha "Pucek", a ponieważ "Pucek" nie jest pustym łańcuchem, atrybut __name obiektu
# przyjmuje wartość "Pucek" i zostaje wyświetlony komunikat "Zmiana imienia się powiodła.".


class Critter(object):
    """Witualny pupil"""

    def __init__(self, name):
        self.name = name
        print("Urodził sie nowy zwierzak")

    @property  # pośredni dostęp (prywatny atrybut)
    def name(self):
        return self.__name

    @name.setter  # atrybut setter dla właściwośni nam sygnalizuje że następująca po dekoratorze definicja metody określi  sposób ustawiania wartości
    def name(self, new_name):
        if new_name == "":
            print("Pusty łańcuch nie może być imieniem zwierzaka.")
        else:
            self.__name = new_name
            print("Zmiena imienia się powiodła")

    def talk(self):
        print("\nCześć Jestem", self.name)


# Część główna
crit = Critter("Reksio")  # Urodził sie nowy zwierzak
crit.talk()  # Imię mojego zwierzaka to: Reksio

print("\nImię mojego zwierzaka to:", end=" ")
print(crit.name)  # Imię mojego zwierzaka to: Reksio

print("\nSpróbuję zmienić imię zwierzaka na Pucek...")
# Spróbuję zmienić imię zwierzaka na Pucek... Zmiena imienia się powiodła
crit.name = "Pucek"

print("\nImię mojego zwierzaka to:", end=" ") 
print(crit.name) # Spróbuję zmienić imię zwierzaka na Pucek...

print("\nPróbuję zmienić imię mojego zwierzaka na pusty łańcuch znaków...")
crit.name = ""

input("Zakończ program Enterem")