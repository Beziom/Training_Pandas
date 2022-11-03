#kwargs - key word arguments
class Monster:

    def __init__(self, health, energy, **kwargs) -> None:
        print(kwargs)
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)

    def attack(self,amount):
        print("The monster has attacked")
        print(f'{amount} of damage was dealt')
        self.energy -= 20

    def move(self,speed):
        print("You have made a step forward")
        print(f"It has a speed of {speed}")

class Fish:

    def __init__(self, speed, has_scales,**kwargs) -> None:
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(kwargs)
    
    def swim(self):
        print(f"The fish is swimming at speed of {self.speed}")

class Shark(Monster,Fish):

    def __init__(self, bite_strength, health, energy, speed, has_scales) -> None:
        self.bite_strength = bite_strength
        super().__init__(health = health, energy = energy, speed = speed, has_scales = has_scales) 

#MRO -> method resolution order (what method parents will call
print(Shark.mro()) # Shark is 0, Monster 1 and fish 2[<class '__main__.Shark'>, <class '__main__.Monster'>, <class '__main__.Fish'>, <class 'object'>]

shark = Shark(15,150,80,15,True)
print(shark.speed)