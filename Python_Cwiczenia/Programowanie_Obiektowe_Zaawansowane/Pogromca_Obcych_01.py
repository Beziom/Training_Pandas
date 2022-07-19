#Pogromca Obcych
#Współdziałanie obiektów

#Obiekty
class Player(object):
    """Gracz w strzelance"""

    def blast(self, enemy):
        print("Gracz razi wroga!")
        enemy.die()

class Alien(object):
    """Obcy w stzelance"""

    def die(self):
        print("Obcy z trudem łapie oddech. Umiera!")

# main
print("Śmierć obcego\n")

hero = Player()
invader = Alien()

hero.blast(invader) 

#Wywoanie metody blast obiektu hero i przekazanie invader - czyli obiektu klasy Alien jako argument.
#Po zbadaniu definicji blast(0 widać że metoda przyjmuje ten obiekt przez swój parametr enemy.)

input("\nNaciśnij enter aby zakończyć program")
