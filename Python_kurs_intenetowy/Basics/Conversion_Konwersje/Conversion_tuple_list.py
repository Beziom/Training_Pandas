#tuple()-krotka,
#list()- lista, 
#set()- zbiór, 
#dict() - słownik

listData = [1,2,3,4,5]
tupleData = tuple(listData) # Utworzenie krotki

print(tupleData)

otherList = list(("Ola", 23, 245)) # Utworzenie lsty

print(otherList)

setData = set(otherList) # Utworzenie zbioru

print(type(setData))
print(setData)

frozenSetData = frozenset(tupleData) # Utworzenie setu
print(type(frozenSetData))
print(frozenSetData)

tupleData = (("Ola", 1234), ("Adam", 2314))
dictData = dict(tupleData)

print(dictData)
