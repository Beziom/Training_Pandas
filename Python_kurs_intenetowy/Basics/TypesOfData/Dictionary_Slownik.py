#contact = {"ANIA" : "Ania@example.com"} - przyklad słownika

contacts = {
    "Ola": "ola@example.com",
    "Daniel": 30,
    "Ania": "ania@example.com"
}

contacts["Rafał"] = "rafal@example.com" # dodanie nowej wartości

print(contacts["Ola"]) # wyświetlenie maila
print(contacts["Daniel"]) # liczba 30

print(type(contacts))

print(len(contacts))

print(contacts.keys()) # Dostępne klucze

print(contacts.values()) # Dostępne wartości

for key in contacts:
    print(key + " " + str(contacts[key])) # Stworzenie pętli w celu wyświetlenia słownia
print(contacts.items())

for key, value in contacts.items(): # Stworzenie pętli w celu wyświetlenia słownika
    print(key, value)

