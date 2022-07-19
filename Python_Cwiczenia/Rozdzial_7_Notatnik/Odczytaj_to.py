#Odczytywanie plików z notatnika
#open(), close(), read(), readline(), readlinse()
# file = r"PATH"
# with()

from cgitb import text
import readline


file = r"c:\Users\Bezio\Desktop\Python\Python_Cwiczenia\Rozdzial_7_Notatnik\Tekst.txt"

print("Otwarcie i zamknięcie pliku")

#otwarcie pliku
TextFile = open(file, "r")

#zamknięcie pliku
TextFile.close()

#odczytywanie znaków z pliku (każy kolejny)
TextFile = open(file, "r")
print(TextFile.read(1))
print(TextFile.read(1))
print(TextFile.read(2))
print()
TextFile.close()

#odczytywanie całego pliku
TextFile = open(file,"r")
WholeFile = TextFile.read()
print(WholeFile)
TextFile.close()

#Odczytywanie znaków z wiersza
TextFile = open(file,"r")
print(TextFile.readline(1))
print(TextFile.readline(1))
print(TextFile.readline(2))
print()
TextFile.close()

#Odczytywanie po jednym wierzu
TextFile = open(file,"r")
print(TextFile.readline(), end = "")
print(TextFile.readline(), end = "")
print(TextFile.readline(), end = "")
print()
TextFile.close()

#Wczytywanie wszystkich wierszy do listy
TextFile = open(file,"r")
TextList = TextFile.readlines()
print(TextList)
TextFile.close()
print()

#Odczytywanie za pomocą pętli
TextFile = open(file,"r")
for i in TextFile:
    print(i, end = "")
TextFile.close()



with open(file) as malpa:
    malpa.readlines()