class Monster():
    """A monster that have some attributes"""    
    def __init__(self, health, energy) -> None:
        """Funciont which innitiae basic arhuments

        Args:
            health (_type_): _description_
            energy (_type_): _description_
        """        
        self.health = health
        self.energy = energy

        #private attributes (_attribute = You shouldn't work with it)
        self._id = 5

    def attack(self,amount):
        print("The monster has attacked")
        print(f'{amount} of damage was dealt')
        self.energy -= 20
        print(self.energy)

    def move(self,speed):
        print("You have made a step forward")
        print(f"It has a speed of {speed}")

monster = Monster(20,10)

"hasattr"
print(hasattr(monster,"health")) # checking if attribute has a attribute

"setattr"
setattr(monster, "weapon", "Sword") #similar to monster.weapon = "Sword"

"example fo setattr"
new_attributes = (["weapon", "Axe"], ["armor", "Shield"], ["potion", "mana"])
for attr,value in new_attributes: 
    setattr(monster,attr,value)

"vars"
print(vars(monster)) #vars provide all attributes

"doc" 
print(monster.__doc__)
print(str.__doc__)
help(monster)