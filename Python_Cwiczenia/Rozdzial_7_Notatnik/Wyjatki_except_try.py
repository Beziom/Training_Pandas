#Demonstracja plików odpornych na błędy

try:
    num = float(input("Wprowadź liczbę: "))
except:
    print("Wystąpił jakiś błąd")
    
print(num)

try:
    num = float(input("Wprowadź liczbę"))
except ValueError: # instrukcja zostanie wykonana wtedy gdy zostanie zgłoszony wyjątek ValueError
    print("To nie jest liczba!")

#obsługa kliku typów wyjątków
print()
for value in (None,"Hej!"):
    try:
        print("Próba konwersji:", value, "-->", end="")
        print(float(value))
    except (TypeError, ValueError):
        print("Wystąpił jakiś błąd!")

#Podwójne użycie Except
print()
for value in (None, "Hej!"):
    try:
        print("Próba konwersji:", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("Możliwa jest tylko konwersja łańcucha lub liczby!")
    except ValueError:
        print("Możliwa jest tylko konwersja łańcucha cyfr!")

#Wykorzystanie argumentu wyjątku (as <zmiennna>)
try:
    num= float(input("Wprowadź liczbę: "))
except ValueError as e:
    print("To nie była liczba! Lub wyrażając to na sposób Pythona")
    print(e) #Przypisany w klauzuli except wartość e

#Dodanie klauzuli else
try:
    num = float(input("Wprowadź liczbę: "))
except ValueError:
    print("To nie była liczba")
else:
    print("Wprowadziłeś liczbę", num)

input("Zakończ program wciskając Enter")