"List unpacking_unlimited arguments"
# * to initiate set unlimited arguments
from unittest import result

from numpy import argsort


def print_all(first,*arguments,extra):
    print("print_all()")
    print(first)
    print(arguments)
    print(extra)
print_all(1,5,2,4,2,3,4,5,2,3,1,extra="dupa")

"Keyword unpacking"
# ** to create dictionary positions
def print_more(**arguments):
    print("print_more()")
    print(arguments)

print_more(arg1 = 1,arg2 ="test",arg3 =[1,2,3])

"Print_master"  

def print_master(*args, **kwargs):
    print("Print_master()")
    print(args)
    print(kwargs)

print_master(1,2,3,4,"it's me", test1 = "dupadupa",test2 = "No i fajnie")

def calculcator(*arg):
    result = sum(arg)
    print(result)

calculcator(1,2,3,4,5,6)