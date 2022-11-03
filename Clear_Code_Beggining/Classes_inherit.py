class Monster:

    def __init__(self, health, energy) -> None:
        self.health = health
        self.energy = energy

    def attack(self,amount):
        print("The monster has attacked")
        print(f'{amount} of damage was dealt')
        self.energy -= 20
        print(self.energy)

    def move(self,speed):
        print("You have made a step forward")
        print(f"It has a speed of {speed}")

class Shark(Monster):

    def __init__(self, health, energy,speed) -> None:
        super().__init__(health, energy)
        super().move(50) # You can super__init nwe versions
        self.speed = speed
    
    def move(self):
        print("The shark has moved")
        print("The speed of the shark is", self.speed)

shark = Shark(150,80,15)

"Excersise"

#Scorpion class which inherint from the monster
#Posion damage atribute - overright damage method to show poision damage

class Scorpion(Monster):

    def __init__(self, health, energy, poison_damage) -> None:
        super().__init__(health, energy)
        self.poison_damage = poison_damage

    def attack(self, amount):
        print("The monster has attacked")
        print(f'{amount} of damage was dealt + additional {self.poison_damage} poison damage')
        self.energy -= 20
        print(self.energy)

scorpion = Scorpion(150,80,15)
scorpion.attack(40)

