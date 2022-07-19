#Nienazwane argumenty funkcja
def printCar(brand, name = "concept", year = "1960", color = "black"):
    print(brand, name, year, color)

#Nienazwane arumenty (bez wskazania parametru)
printCar("Ford")
printCar("Ford", "Mustang")
printCar("Ford", "Mustang", "1970")
printCar("Ford", "Mustang", "1970", "Red")

print("\n")

#Nazwane argumenty
def printCar(brand, name = "concept", year = "1960", color = "black"):
    print(brand, name, year, color)

printCar(name = "T",brand = "Ford")
printCar(name = "T",brand = "Ford", year = "1920")

#/ ogarniczają sposoby przekazywania danych do funkcji, nie można uzywac nazwanych
#* ogarniaczją sposoby przekazywania danych do funkcji, musza być nazwane