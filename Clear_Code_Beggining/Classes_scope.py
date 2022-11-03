#scope problem

"Trying to update value health by function"
def update_health(amount):
    global health
    monster.health += amount
#function will not update health if health is not global

"Trying to update value monste.health by creating health attribute"
class Monster:
    def __init__(self,health,energy):
        self.health = health
        self.energy = self.set_enery(energy)

    def update_energy(self,amount):
        self.energy += amount

    def set_enery(self,energy):
        new_energy = energy*2
        return new_energy

    def get_damage(self,amount):
        self.health -= amount

monster = Monster(100,50)
monster.health +=20
print(monster.health) # 120
update_health(40)
print(monster.health) # 160
monster.update_energy(20)
print(monster.energy) # 120 because 50 * 2 (set_energy) + 29 from udpate

"Excersise"
#1. Create a hero class with 2 parameters: damage, monster
#2. The monster clas should gavee a method that lowers the health -> get_damae(amount)
#3. The hero class should have an attack meethod that calls the get-Damahe method from Monster
# The amunt of damage is hero.damae

class Hero:

    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster

    def attack(self):
        self.monster.get_damage(self.damage)

hero = Hero(15,"Marcinek")
monster.get_damage(15)
print(monster.health)

        
