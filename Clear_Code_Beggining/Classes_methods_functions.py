"All in python are object = here YOu can check how to add an function to created class"
# def add(a,b): # Method is an object
#     return a + b

# class Test:
#     def __init__(self,add_function):
#         self.add_function = add_function

# test = Test(add)
# print(test.add_function(1,2))
# print(dir(test))

"Monaster class with parameter"
#Monster class
#Parameter called func (store func as parameter)
#Another class clled Attacks which have 4 methods: bite, strike, slash, kick (just print)

#Creata a monster object and give it one of the attack method from the arrack class

class Monster(object):
    def __init__(self,func):
        self.func = func

class Attacks(object):
    def bite(self):
        print("Monster has bitted enemy!")
    def strike(self):
        print("Monster has stiked enemy!")
    def slash(self):
        print("Monster has slashed enemy!")
    def kick(self):
        print("Monster has kicked enemy!")

monster1 = Monster(Attacks().bite)
monster1.func() # if we dont give bracket to Attacks().bite then TypeError: """Attacks.bite() missing 1 required positional argument: 'self'"""" will appear
