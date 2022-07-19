# Inwentarz Bohetera - krotki

inventory = () # Pusta krotka 

if not inventory:
    print("Masz puste ręcę") # Wskazanie że pusta krotka = nic

input("Aby kontynuować misję, naciśnij klawisz Enter")

inventory = ("miecz", "zbroja", "tarcza", "napój uzdrawiający")
print("\nWykaz zawartości krotki:","\n", inventory)

print("\nElementry Twojego wyposażenia:")
for i in inventory:
    print(i)

input("Aby zakończyć wcisnij enter")
