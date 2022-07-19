#Analizator komunikatów - długości tekstu

message = input("Wprowadź komunikat!")

print("Długość Twojego komunikatu wynosi", len(message)) # LEN(długość znaków)
print("Najczęście używana litera w jęzuku polskim, 'a'.")
if "a" in message: # in jako sprawdzenie czy jakiś elemnent jest zawarty
    print("Występuje, w komunikacie")
else:
    print("nie wystąpiła w Towim komunikacie.")

input("\n\n Aby zakończyć program wciśnij Enter")
