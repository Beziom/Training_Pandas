class Monster:

    def __init__(self,health,energy) -> None:
        self.health = health
        self.energy = energy

    def __len__(self): #If len will be used it will return 5
        return self.health

    def __abs__(self):
        return self.energy

    def __call__(self):
        print("Monster was called")

    def __add__(self,other):
        return self.health + other
    
    def __str__(self):
        return "DupaDupa"

    #methods
    def attack(self,amount):
        print("The monster has attacked")
        print(f'{amount} of damage was dealt')
        self.energy -= 20
        print(self.energy)

    def move(self,speed):
        print("You have made a step forward")
        print(f"It has a speed of {speed}")

monster1 = Monster(10,20)
print(len([1,2,3,4,5,6,7,8]))
print(len(monster1))
print(abs(monster1))
print(dir(monster1)) # Dir shows all possible functions related to object and functions
print(monster1.__dict__) # showing attributes in dict
print(vars(monster1) )# showing attributes in dict
monster1() # After using __call__ method
print(monster1 + 10) # after __add__ method
print(monster1) # aftr __str__ method