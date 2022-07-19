
data = ("Ala", "Ola", "Kasia") # Krotki są niemutowalne ( zmiana po indeksie da błąd)
print(data)
names = data + ("Rafał",) # Dodając element musiy uwzględnić przecinek
print(names)
print(len(names)) # Zwracanie ilości elementów
print(type(names))

numbers = 1,2,3
print(type(numbers))

emptyTuple = () # Pusta krotka
print(emptyTuple)

print(names[1]) # OLA
print(names[1:3]) #Ola, Kasia

cars = (("Dodge", "Ford"), ("Pontiac")) # Krotka wielopoziomowa
print(cars)
print(cars[0][0]) # Argument 0 podpoziomu 0
if "Ford" in cars[0]:
    print("Ford w krotce")
if "Ford" in cars[1]:
    print("Ford w krotce")

del cars # Usuwanie krotki

# del name [0} NIE BĘDZIE DZIAŁĄĆ

tupleX3 = names * 3
print(tupleX3)
