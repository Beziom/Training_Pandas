#Inwentarz bohatera 2.0 

inventory = ("miecz", # Wypisanie krotki
"zbroja",
"tarcza",
"napój uzdrawiający")

print("Elementy Twojego inwentarza:")
print()
for item in inventory: # Wymienienie itemów
    print(item)

input("\nAby kontynować grę naciśnij Enter")

print("Twój dobytek zawiera", len(inventory), "elementy(-ów).") #Wymiana elementów w krotce

input("\nAby kontynować grę, naciśnij Enter.")

if "napój uzdrawiający" in inventory: # Sprawdzanie czy element jest w krotce
    print("Dożyjesz dnia w któym stoczysz walkę")

index = int(input("\nWprowadź indeks elementu inwentarza: "))
# 1- miecz, 2- zbroja, 3- tarcza, 4- napój uzdrawiający

print("Pod indekrsem", index, "znajduje się", inventory[index])

#Wycinek
start = int(input("Wprowadź indeks początka wycinka"))
finish = int(input("Wprowadź indeks końca wycinka"))
print("inventory[", start, ":", finish, "] to", end="") 
print(inventory[start:finish]) #Inventory 1:3

input("\nAby kontynuować grę, naciśnij klawisz Enter")

chest = ("złoto", "klejnoty") #Dodanie nowych rzeczy do krotek
print("Znajdujesz skrzynię, któa zawiera:")
print(chest)
print("Dodajesz zawartość skrzyni do swojego inwentarza.")
inventory += chest
print("Twój aktualny inwentarz to:", inventory)

input("Aby zakończyć program naciśnij klawisz Enter")







          




