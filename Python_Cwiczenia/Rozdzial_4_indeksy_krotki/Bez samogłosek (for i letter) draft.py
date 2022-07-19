#Bez samogłosek (omijanie samogłosek w omijanym tekście)

message = input("Wprowadź omunikat z którego mają być usunięte samogłoski")
new_message = ""
VOWELS = "aąeęioóuy"

print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("Został utworzony nowy łańcuch", new_message)

print("\nTwój komunikat bez samogłosek to:", new_message)
