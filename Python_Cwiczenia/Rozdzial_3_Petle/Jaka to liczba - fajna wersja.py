# Jaka to liczba
import random
numer1 = int(input("Cześć, wybierz liczbę od 1 do 100"))
mumer2 = random.randint(1,100)
tries = 1
             
while numer1 != mumer2:
    if numer1 > mumer2:
        print("\nTwoja liczba jest za duża, podaj mniejszą")
        numer1 = int(input("\nOdganij liczbę znowu"))
        tries += 1
    else:
        print("\nTwoja liczba jest za mała")
        numer1 = int(input("\nOdganij liczbę znowu"))
        tries += 1
                     
print("Gratulacje, udało Ci się za", tries, "razem")
input("Zakończ enterkiem")

        
