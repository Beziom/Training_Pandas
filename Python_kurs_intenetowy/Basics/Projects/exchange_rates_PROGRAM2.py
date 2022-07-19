# Json to format odczytywany przez wiele języków, ale trzeba go przerobić

import requests # moduł pobierania danych

response = requests.get("https://api.nbp.pl/api/exchangerates/tables/a?format=json") # import danych ze strony

if response.ok == True: # Jeśli odpowiedź jest prawidłowa nie zwróci błędu
    data = response.json() [0] # wchodzimy w słownik
    print(data)
    print(type(data))

    table = data["table"]
    no = data["no"]
    effectiveDate = data["effectiveDate"]
    print("\nExchange rates:", table, no, effectiveDate)

    rates = data["rates"]
    
    for rate in rates:
        currency = rate["currency"]
        code = rate["code"]
        mid = rate["mid"]
        print(currency, "code:", code, "value", mid)
