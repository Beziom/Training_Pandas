#Funkcja dla słownika

data = {"name": "Ola", "city": "Waw"}
print(data["name"])

#dodanie do słownika
dataPostalCode = "postalCode"
data[dataPostalCode] = "12345"
print(data)

#długość słownika
print(len(data)) #3 elementy3 klucz i 3 wartości

#usunięcie elementu
del data["city"]
print(data)

#usunięcie wszystkiego
data.clear()

data = {"name": "Kasia", "city": "Krk"}

#utworzenie kopii
dataCopy = data.copy()
print(dataCopy)

print(data["name"] is dataCopy["name"]) # teo samo odwołanie do pamięci
print(data is dataCopy) # False - różnią się, różne miejsca w pamięci

#nowy słownik
data2 = dict.fromkeys(("name", "city", "code"))
print(data2)

#nowy słownik (z domyślną wartością)
data3 = dict.fromkeys(("name", "city", "code"), 0)
print(data3)

print(data2.get("x", "DEFAULT")) #DEFAULT

print("name" in data2) # Istnieje name w data 2 czyli True

#Wyświetlanie zawartości
print(data2.keys())
print(data2.values())