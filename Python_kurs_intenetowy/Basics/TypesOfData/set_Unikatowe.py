#Nie pozwala na dodanie zdupliowanych elementów, jest iterowalny, zmienny i nie posiada elementów pozycji
#frozen set jest niemutowalny
#Przewaga UNIKALNEJ POZYCJI
#set = {1,2,3,4,5,6}

setData = {2,3,1,4,5}
setData.add(22) # dodanie liczby 22 
setData.discard(1) # usunięcie jedynki

print(type(setData))
print(len(setData)) # 5 elementów
print(setData)

for v in setData:
    print(v)

frozenData = frozenset(setData) # Dokonanie konwercji na odporny set

print(type(frozenData)) #frozenset
#frozenData.add(56) wywali błąd
print()
for value in frozenData:
    print(value)



