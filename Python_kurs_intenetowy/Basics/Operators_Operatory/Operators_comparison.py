# Operatory porównania
# !=, ==, >, <, >=, <=

# Operatory logiczne
# and, or, not

# Operatory przynależności
# in, not in (są czy nie są w sekwencji danych)

# Operatory tożsamości
# is, is not (porównanie lokalizacji w pamięci operandów)

# Operator konkatenacji
# "+" do łączenia znaków list i zbiorów
print(True and False)
print(True or False)

taskCompleted = True
linesOfCodeWritten = 100

if taskCompleted == True and linesOfCodeWritten >= 50:
    print("Go home")

print(not True)

#operatory przynależności
data = [0,1,2,3,4,5]
print(-1 in data) # False
print(3 in data) # True
print("3" in ("3", "4"))

print(10 not in data)

#operatory identity operators
strData = "test"
print(dir(strData))
print(strData.upper())
intData = 10
print(dir(intData))
a = [1,2,3,4,5]
b = a
print(a is b) # referencja (to samo miejse w pamięci)
a.append(77)
print(a)
print(b)
print(a is not b) #False
c = [3,4,5]
print (a is c)# False

#Konkatenacja

strData = "Hello" + "World"
print(strData)
print(strData + " and Hello again!")

listData = [1,2,3]
print(listData + [4,5,6])


