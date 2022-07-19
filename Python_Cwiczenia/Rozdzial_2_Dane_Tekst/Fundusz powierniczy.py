# Uczestnik funduszu powierniczego - poprawna wersja
# Demonstruje błąd logiczny

print(
"""
            Uczestnik funduszu powierniczego
Sumowanie Twoich miesięcznych wydatków na to żeby się nie bać i być spokojnym

Wprowadź swoje wymagane miesięczne koszty.  Ponieważ jesteś bogaty, zignoruj
grosze i swoje kwoty podaj w pełnych złotych.

"""
)

car =  int(input("Serwis Mercedesa: ")) # int zapobiega temu żeby końcowe sumowanie było tekstem (nadajemy wartość)
rent = int(input("Apartament w Śródmieściu: "))
jet = int(input("Wynajem prywatnego samolotu: "))
gifts = int(input("Podarunki: "))
food = int(input("Obiady w restauracjach: "))
staff = int(input("Personel (służba domowa, kucharz, kierowca, asystent): "))
guru = int(input("Osobisty guru i coach: "))
games = int(input("Gry komputerowe: "))

total = car + rent + jet + gifts + food + staff + guru + games

print("\nOgółem:", total)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

