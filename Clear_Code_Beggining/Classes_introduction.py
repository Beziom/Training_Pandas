class Monster:

    #atributes
    health = 90
    energy = 40

    #methods
    def attack(self,amount):
        print("The monster has attacked")
        print(f'{amount} of damage was dealt')
        self.energy -= 20
        print(self.energy)

    def move(self,speed):
        print("You have made a step forward")
        print(f"It has a speed of {speed}")

monster = Monster()
print(monster.health)
print(monster.energy)
monster.attack(40)
monster.move(10)
