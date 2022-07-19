#False Zera i puste krotki/liczby dają false, None też daje False
#True - wartości różne od zera albo jakikolwiek element w liście,krotce (nawet jeśli zero)

#Falsy Values
print(bool(False))
print(bool())
print(bool(0))
print(bool(0.0))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(""))
print(bool(None))

#True values
print(bool(True))
print(bool(1))
print(bool(-2))
print(bool((1)))
print(bool([0]))
print(bool({0}))
print(bool("1"))

currentTaskNumber = 10
currentTaskNumber = None # Nie ma zadania do zrobienia
print(currentTaskNumber)
currentTaskNumber = 14
print(currentTaskNumber)
