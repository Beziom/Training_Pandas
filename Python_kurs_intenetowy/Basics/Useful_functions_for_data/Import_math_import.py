import math
import random

#wartość bezwzględnia
print(abs(-5))

#zaokrąglenie do najmniejszej liczby całkowitej nie mniejszej niż podane wartości
print(math.ceil(6.78)) # 7
print(math.ceil(20.12)) # 21
print(math.ceil(-3.23))

#zaokrąglenie do największej liczby całkowitej nie większej niż podane wartości
print(math.floor(6.78))
print(math.floor(20.12)) # 20
print(math.floor(-3.23)) # -4

#największa wartość
print(max((10,1,-9,33,89))) # 89 
print(max([10,1,-9,33,89])) # 89 
print(max({10,1,-9,3,89})) # 89 

#najmniejsza wartość
print(min((10,1,-9,33,89))) # 89 
print(min([10,1,-9,33,89])) # 89 
print(min({10,1,-9,3,89})) # 89 

#podniesienie do potęgi
print(pow(4,3)) # 4 do potęgi 3

#pierwiastek
print(math.sqrt(128)) # 11.31 

#zaokrąglanie
print(round(12.782313872, 3)) # zaokrąglenie do 3 miejsc po przecinku

#liczba zmiennoprzecinkowa od 0 do 1
print(random.random()) 
print(int(random.random() * 100)) # Liczba od 1 do 100

#losowy wybór
print(random.choice([0,1,2,3,4,5]))
print(random.choice(["Ania", "Ola", "Basia"]))

#losowa wartość z zakresu co ileś
print(random.randrange(-10, 30, 5))

#losow elementy w liście
listData = [0,1,2,3,4,5]
random.shuffle(listData)
print(listData)