#Zapisz to
#Demonstruje zapisywanie danych do pliku tekstowego

#Wskazanie ścieżki i zapisanie pliku "w"
#usuwanie pliku z pythona
import os

file = r"c:\Users\Bezio\Desktop\Python\Python_Cwiczenia\Rozdzial_7_Notatnik\zapisz_to.txt"
TextFile = open(file, "w")

#Dodanie tekstu do notatnika
TextFile.write("Wieresz 1\n")
TextFile.write("To jest wiersz 2\n")
TextFile.write("A to jest wiersz 3\n")
TextFile.close()

#Odczytanie programu
TextFile = open(file, "r")
print(TextFile.read())
TextFile.close()

#Zapisanie za pomoca listy
TextFile = open(file, "w")
TextFile.close()
os.remove(r"c:\Users\Bezio\Desktop\Python\Python_Cwiczenia\Rozdzial_7_Notatnik\zapisz_to.txt")