#Bez samogłosek (omijanie samogłosek w omijanym tekście)

message = input("Wprowadź komunikat")
new_message = ""                                                # Wartownik
VOWELS = "aąeęiouóy"                                            # Lista samogłosek
print()                                                         # Dodanie sztuego akapitu
for i in message:                                               # Pętla for dla wypunktowania wszystkich zmian
    if i.lower() not in VOWELS:                                 # każda litera zostaje zmieniona na mniejszą i nie zawiera się w liście
        new_message += i                                        # Do nowej wiadomości zostaje dodana wypunkotwana wartość
        print("Został utworzony nowy znak: ", new_message)

print("\n Twój komunikat bez samogłosek to:", new_message)
input("Zakończ Enterkiem")
