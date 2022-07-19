#Program przedstawia dokonywanie zmian w inwentarzu Bohatera

inventory = ["miecz", "zbroja", "tarcza", "napój uzdrawiający"]

#wyswietlenie aktualnego ewipunku
print("Elementy Twojego inwentarza:")
for i in inventory:
    print(i)

#Ilość przedmiotów w plecaku
print("\nTwój dobytek zawiera", len(inventory), "elementów")

#Czy masz potiony na walkę?
if "napój uzdrawiający" in inventory:
    print("Przeżyjesz następną walkę ponieważ masz", inventory[3])


index = int(input("Wpisz indeks aby sprawdzić co kryje się w plecaku: "))
print(inventory[index])

input("\nWciśnij Enter aby zakończyć program")
