"@property function"
from datetime import datetime

"First attempt wihout decorator"
# class Generic:
#     def __init__(self) -> None:
#         self._x = 10
    
#     def getter(self): #whenever getter is called
#         print(datetime.now())
#         print("Get_x")
#         return self._x
    
#     def setter(self,value):
#         print("Set_x")
#         self._x = value

#     def deleter(self):
#         print("Delete_x")
#         del self._x

#     x = property(getter,setter,deleter)#property(getter,setter,deleter)

"With Decorator"

class Generic:
    def __init__(self) -> None:
        self._x = 10
    @property
    def x(self): #whenever getter is called
        print(datetime.now())
        print("Get_x")
        return self._x
    
    @x.setter
    def x(self,value):
        print("Set_x")
        self._x = value

    @x.deleter
    def x(self):
        print("Delete_x")
        del self._x

generic = Generic()
generic.x = 4
print(generic.x)
del generic.x
