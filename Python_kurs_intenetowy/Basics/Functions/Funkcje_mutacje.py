#Wykonywanie funkcji na niemutowalnych typów sprawia że nie zostaje ona trwale ustalana (wynikiem końcowym jest oryginalna zmienna) (2) --> funkcja (+2) = 2
#Mutowalne są trwale zmieniane [2] --> funkcja [4,4,4] --> [2,4,4,4]

#immutable: int, float, bool, string, str, frozenset (utworznoy nowy twór w pamięci)

#uchwyt do pamięci nazywamy referencją (referencja zostałą zmieniona do nowego miejsca w pamięci)

#modyfikacja niemutowalnej zmiennej
def modifyStr(strData):
    print(id(strData))
    strData += "!"
    print(id(strData))#inna wartość po modyfikacji
    print(strData) # wyświetlenie "Hello!"

string = "Hello"

modifyStr(string)
print(string) # wartość dla str się nie zmieniła = "Hello"

#modyfikacja mutowalnej zmiennj
def modifylist(listData):
    print(id(listData))#id to samo
    listData.append(10)
    print(id(listData))#id to samo
    
listValue = [1,5,9]
print(id(listValue))#id to samo
modifylist(listValue)
print(listValue)



