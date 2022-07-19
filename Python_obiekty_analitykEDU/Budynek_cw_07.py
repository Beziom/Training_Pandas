class Building(object):
    """Skeleton for buildin"""
    __people = 0

    def __init__(self, people, name):
        self.__people = people
        self.name = name
        print("There is a new building named:", name)

    def entering(self):
        self.__people += 1
        print("Someone has entered the Building")

    def leaving(self):
        if self.__people <= 0:
            print("No people in the building")
        else:
            self.__people -= 1
            print("Someone has left the building")

b1 = Building(5,"Enterprise Park")
b1.entering()
b1.leaving()
b1.leaving()
b1.leaving()
b1.leaving()
b1.leaving()
b1.leaving()
b1.leaving()
