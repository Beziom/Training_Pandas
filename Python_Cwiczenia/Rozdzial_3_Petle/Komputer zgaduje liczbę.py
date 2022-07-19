# Jaka to liczba - komputer
import random
numer1 = int(input("Wybierz liczbę od 1 do 100"))
numer2 = random.randint(1,100)
tries = 1
while numer1 != numer2:
    if numer1 > numer2:
        numer2 = random.randint (numer1,100)
        tries += 1
        print("Wynik", numer2, "próba", tries)
    else:
        numer2 = random.randint (1,numer1)
        tries += 1
        print("Wynik", numer2, "próba", tries)
print("Komputer odgadł za", tries, "razy")
input("Zakończ enterkiem")
