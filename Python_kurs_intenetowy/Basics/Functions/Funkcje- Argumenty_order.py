#/ ogarniczają sposoby przekazywania danych do funkcji, nie można uzywac nazwanych (przed slashem)
#* ogarniaczją sposoby przekazywania danych do funkcji, musza być nazwane (za gwiazdką)

def printCar(brand, / , name = "concept", * ,year = 1960, color = "black"): #wzystko przed slashem jako pozycyjny, a wszystko przed gwiazdką jako nazwany
    print(brand, name, year, color)

printCar("Ford", "Mus", year = 1973, color = "blue")
printCar("Ford", "Mus", color = "blue", year = 1973)
#printCar(brand = "Ford", "Mus", color = "blue", year = 1973) = błąd

