#Łączenie znaków
print("Hello" + "World")

#Indeksowanie
string = "Hello World!"
print(string[0]) # H
print(string[0:5]) # Hello

#sprawdzanie cyz coś znajduje się w łańuchy
print("Hello" in string) # True
print("Hello" not in string) # False

#wielozdanie
multiline = """ line1
line2
line3"""

#Duże litery na samym początku
print("ala".capitalize()) # Ala

#Liczenie wystąpień łańcucha
print("Ola ma kota, Ola ma psa, Ola to kozak".count("Ola")) # 3

#Wycentrowania łańcycha
print("Hello".center(20,"-")) #-------Hello--------

#Sprawdzania czy łańcuch zaczyna się wpisanym łańcuchem
print(string.startswith("Hello")) #True
print(string.endswith("Hello")) #False
print(string.endswith("World!")) #True

#Szukanie od lewej czy występuje dany łańcuch (-1 jeśli nie), wartość indeku jeśtli tak
print(string.find("World!")) # 6 indeks
print(string.find("Cyk")) # -1

#szukanie od prawej
print("Ola ma kota, Ola ma psa, Ola to kozak".rfind("Ola")) # 25 indeks

#liczba całkowita
print("12893129381".isalnum()) #Tak
print("12893129381 k".isalnum()) #Nie
print("12893129381.123123".isalnum()) #Nie

#Sprawdzania czy listera alfabetu
print("Tak".isalpha()) #Tue
print("Tak ".isalpha()) #False

#Sprawdzanie czy z małych czy z dużych
print("test".islower())#True
print("tesT".islower())#False
print("TEST".isupper())#True

#Czy jest spacja (tabulator albo nowa linia)
print(" ".isspace())#True
print("\n".isspace())#True
print("\t".isspace())#True

#Zawartość w liście można połączyć
print("-|".join(["Ala", "Ola", "Adam"])) # Ala-|Ola-|Adam

#Wielkości liter
print("Hello World".lower()) # hello world
print("Hello World".upper()) # HELLO WORLD
print("Hello World".swapcase()) # HELLO WORLD

#Pozbywanie się białych znaków
print(" \n\t Hello World \n\n \t".lstrip()) #usunięcie znaków z lewej strony
print(" \n\t Hello World \n\n \t".rstrip()) #usunięcie znaków z prawej strony
print(" \n\t Hello World \n\n \t".strip()) #usunięcie znaków z lewej i prawej strony

#Zamiana znaków
print("Ola ma psa, Ola ma kota".replace("Ola", "Kasia")) #Kasia ma psa, Kasia ma kota

#Formatowanie danych (Tworzenie długich zdań)
print("My name is {myName}, I'm from {country}".format(myName = "Kuba", country = "Poland" ))
print("My name is {0}, I'm from {1}".format("Kuba","Poland" ))

#Liczenie ilości liter
print("Hello World Madagdala".count("l"))#4




