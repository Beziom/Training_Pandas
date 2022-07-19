#iterowanie sekwencji jak listy, krotki, słownika, zbioru czy łańcucha
#działa również else
#range
for v in [1,2,3,4]:
    print(v*2)

for v in ("Ania", "Ola", "Rafał"):
    print(v)

for v in {3,4,5,6,"Ola"}:
    print(v)

for v in "Hello":
    print(v)
else:
    print("Pętla zakończona")

dictionaryData = { "Ania": "ania@example.com", "Adam": "adam@example.com"}
print()
for key in dictionaryData:
    print(key)
print()
for key in dictionaryData.keys(): # Wywołanie kluczy
    print(key)
print()
for key in dictionaryData.keys(): # Wywołanie wartości
    print(dictionaryData[key])
print()
for key in dictionaryData.values(): # Wywołanie wartości
    print(key)
print()
for key, value in dictionaryData.items(): # Wywołanie wartości i kluczy
    print(key, ":", value)

#range
for v in range(5): #liczenie do 4
    print(v)
print()

for v in range(3,6): # liczenie od 3 do 5
    print(v)
print()

for v in range(2,9,2): #liczenie od 2 do 9 co 2
    print(v)

